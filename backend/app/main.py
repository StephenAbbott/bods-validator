from __future__ import annotations

import os
from pathlib import Path
from typing import Union
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import httpx

from .validator import validate_bods_data
from .examples import get_examples, get_example_by_id

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
    data = await request.json()
    result = validate_bods_data(data)
    return result


@app.post("/api/validate/file")
async def validate_file(file: UploadFile = File(...)):
    if file.size and file.size > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413, detail="File too large. Maximum size is 10MB."
        )

    content = await file.read()
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")

    result = validate_bods_data(data)
    return result


@app.post("/api/validate/url")
async def validate_url(request: URLRequest):
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(request.url)
            response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400, detail=f"Could not fetch URL: {str(e)}"
        )

    try:
        data = response.json()
    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(
            status_code=400, detail=f"URL did not return valid JSON: {str(e)}"
        )

    result = validate_bods_data(data)
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
