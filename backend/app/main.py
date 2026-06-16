from __future__ import annotations

import ipaddress
import json
import socket
from pathlib import Path
from urllib.parse import urlparse

import httpx
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .validator import validate_bods_data
from .examples import get_examples, get_example_by_id

# Maximum accepted payload size, applied consistently to every input method
# (paste, file upload, URL fetch) so no path can push an unbounded amount of
# data into memory and the (synchronous) validator.
MAX_INPUT_BYTES = 10 * 1024 * 1024  # 10 MB
MAX_INPUT_MB = MAX_INPUT_BYTES // (1024 * 1024)


def _assert_within_size_limit(num_bytes: int) -> None:
    if num_bytes > MAX_INPUT_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"Data too large. Maximum size is {MAX_INPUT_MB}MB.",
        )


def _assert_safe_fetch_url(url: str) -> None:
    """Reject URLs that could be used for SSRF before any request is made.

    Only http(s) is allowed, and the host must not resolve to a private,
    loopback, link-local, or otherwise non-global address. This stops the
    server being tricked into fetching internal services (e.g. cloud metadata
    endpoints like 169.254.169.254 or http://localhost/...).
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise HTTPException(
            status_code=400,
            detail="Only http and https URLs are supported.",
        )
    host = parsed.hostname
    if not host:
        raise HTTPException(status_code=400, detail="URL has no host.")

    try:
        addr_infos = socket.getaddrinfo(host, parsed.port or None)
    except socket.gaierror:
        raise HTTPException(
            status_code=400, detail=f"Could not resolve host: {host}"
        )

    for info in addr_infos:
        ip = ipaddress.ip_address(info[4][0])
        if not ip.is_global or ip.is_link_local or ip.is_reserved:
            raise HTTPException(
                status_code=400,
                detail="URL resolves to a non-public address and cannot be fetched.",
            )

app = FastAPI(title="BODS Validator", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve built frontend in production
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"


class URLRequest(BaseModel):
    url: str


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.get("/api/examples")
async def examples():
    return get_examples()


@app.get("/api/examples/{example_id}")
async def example_detail(example_id: str):
    example = get_example_by_id(example_id)
    if not example:
        raise HTTPException(status_code=404, detail="Example not found")
    return example


@app.post("/api/validate")
async def validate_json(request: Request):
    body = await request.body()
    _assert_within_size_limit(len(body))
    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
    # validate_bods_data is synchronous and CPU-bound; run it in a worker
    # thread so it doesn't block the event loop (and other requests).
    result = await run_in_threadpool(validate_bods_data, data)
    return result


@app.post("/api/validate/file")
async def validate_file(file: UploadFile = File(...)):
    if file.size:
        _assert_within_size_limit(file.size)

    content = await file.read()
    _assert_within_size_limit(len(content))  # guard when size header is absent
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")

    result = await run_in_threadpool(validate_bods_data, data)
    return result


@app.post("/api/validate/url")
async def validate_url(request: URLRequest):
    _assert_safe_fetch_url(request.url)

    chunks: list[bytes] = []
    total = 0
    try:
        # Do not follow redirects: a redirect could point at an internal host
        # and bypass the SSRF check above. Stream so we can stop at the cap
        # instead of buffering an unbounded response.
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=False) as client:
            async with client.stream("GET", request.url) as response:
                response.raise_for_status()
                async for chunk in response.aiter_bytes():
                    total += len(chunk)
                    _assert_within_size_limit(total)
                    chunks.append(chunk)
    except HTTPException:
        raise
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400, detail=f"Could not fetch URL: {str(e)}"
        )

    try:
        data = json.loads(b"".join(chunks))
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(
            status_code=400, detail=f"URL did not return valid JSON: {str(e)}"
        )

    result = await run_in_threadpool(validate_bods_data, data)
    return result


# --- Serve frontend static files in production ---
if FRONTEND_DIR.exists():
    # Mount static assets (JS, CSS, images)
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIR / "assets"), name="assets")
    app.mount(
        "/bods-images",
        StaticFiles(directory=FRONTEND_DIR / "bods-images"),
        name="bods-images",
    )
    app.mount(
        "/lib", StaticFiles(directory=FRONTEND_DIR / "lib"), name="lib"
    )

    @app.get("/{path:path}")
    async def serve_spa(path: str):
        """Serve the SPA — return index.html for all non-API, non-asset routes."""
        file_path = FRONTEND_DIR / path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(FRONTEND_DIR / "index.html")
