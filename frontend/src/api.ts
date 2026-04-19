import type { ValidationResult, ExampleSummary, Example } from "./types";

const API_BASE = "/api";

export async function validateJson(data: any): Promise<ValidationResult> {
  const res = await fetch(`${API_BASE}/validate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || "Validation failed");
  }
  return res.json();
}

export async function validateFile(file: File): Promise<ValidationResult> {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch(`${API_BASE}/validate/file`, {
    method: "POST",
    body: formData,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || "Validation failed");
  }
  return res.json();
}

export async function validateUrl(url: string): Promise<ValidationResult> {
  const res = await fetch(`${API_BASE}/validate/url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || "Validation failed");
  }
  return res.json();
}

export async function fetchExamples(): Promise<ExampleSummary[]> {
  const res = await fetch(`${API_BASE}/examples`);
  if (!res.ok) throw new Error("Failed to fetch examples");
  return res.json();
}

export async function fetchExample(id: string): Promise<Example> {
  const res = await fetch(`${API_BASE}/examples/${id}`);
  if (!res.ok) throw new Error("Failed to fetch example");
  return res.json();
}
