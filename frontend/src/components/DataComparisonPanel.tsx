import { useState } from "react";

interface Props {
  originalData: any;
  originalFormat: string;
  bodsData: string;
  exampleId?: string;
}

function downloadJson(content: string, filename: string) {
  const blob = new Blob([content], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

function DownloadButton({ onClick, label }: { onClick: () => void; label: string }) {
  return (
    <button
      onClick={onClick}
      title={`Download ${label}`}
      className="inline-flex items-center gap-1 text-xs transition-colors font-mono"
      style={{ color: "var(--oo-blue)", fontSize: 11 }}
    >
      <svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
        <path d="M8 2v8m0 0l-3-3m3 3l3-3M3 12h10" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      JSON
    </button>
  );
}

export default function DataComparisonPanel({
  originalData,
  originalFormat,
  bodsData,
  exampleId,
}: Props) {
  const [view, setView] = useState<"side-by-side" | "original" | "bods">(
    "side-by-side"
  );

  const prefix = exampleId ? `${exampleId}-` : "";
  const originalFilename = `${prefix}original-data.json`;
  const bodsFilename = `${prefix}bods-0.4.json`;

  const originalJson = JSON.stringify(originalData, null, 2);

  const tabClass = (_v: string) =>
    `px-3 py-1.5 text-xs font-medium transition-colors`;

  return (
    <div
      className="bg-white shadow-sm"
      style={{ borderRadius: 10, border: "1px solid var(--oo-rule)" }}
    >
      <div className="p-4" style={{ borderBottom: "1px solid var(--oo-rule)" }}>
        <div className="flex items-center justify-between flex-wrap gap-2">
          <div className="flex items-center gap-2">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              fill="none"
              style={{ color: "var(--oo-blue)" }}
            >
              <rect x="1" y="2" width="7" height="16" rx="1" stroke="currentColor" strokeWidth="1.5" />
              <rect x="12" y="2" width="7" height="16" rx="1" stroke="currentColor" strokeWidth="1.5" />
              <path d="M8 10h4" stroke="currentColor" strokeWidth="1.5" strokeDasharray="2 2" />
            </svg>
            <h3 className="font-bold" style={{ color: "var(--oo-navy)" }}>
              Data Mapping: {originalFormat} &rarr; BODS 0.4
            </h3>
          </div>
          <div className="flex gap-1">
            <button
              className={tabClass("side-by-side")}
              style={{
                borderRadius: 6,
                background: view === "side-by-side" ? "var(--oo-blue)" : "transparent",
                color: view === "side-by-side" ? "#fff" : "var(--oo-muted)",
              }}
              onClick={() => setView("side-by-side")}
            >
              Side by Side
            </button>
            <button
              className={tabClass("original")}
              style={{
                borderRadius: 6,
                background: view === "original" ? "var(--oo-blue)" : "transparent",
                color: view === "original" ? "#fff" : "var(--oo-muted)",
              }}
              onClick={() => setView("original")}
            >
              {originalFormat}
            </button>
            <button
              className={tabClass("bods")}
              style={{
                borderRadius: 6,
                background: view === "bods" ? "var(--oo-blue)" : "transparent",
                color: view === "bods" ? "#fff" : "var(--oo-muted)",
              }}
              onClick={() => setView("bods")}
            >
              BODS 0.4
            </button>
          </div>
        </div>
        <p className="text-xs mt-2" style={{ color: "var(--oo-muted)", lineHeight: 1.7 }}>
          See how the original data format maps to the Beneficial Ownership Data
          Standard. This demonstrates how country-specific beneficial ownership
          data can be standardised for interoperability.
        </p>
      </div>

      <div className="p-4">
        {view === "side-by-side" && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span
                  className="text-xs font-semibold uppercase"
                  style={{ letterSpacing: "0.1em", color: "var(--oo-muted)" }}
                >
                  {originalFormat}
                </span>
                <span className="text-xs bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded">
                  Original
                </span>
                <DownloadButton onClick={() => downloadJson(originalJson, originalFilename)} label="original data" />
              </div>
              <pre
                className="text-xs p-3 overflow-auto max-h-80 font-mono"
                style={{ background: "var(--oo-bg)", borderRadius: 8, border: "1px solid var(--oo-rule)" }}
              >
                {originalJson}
              </pre>
            </div>
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span
                  className="text-xs font-semibold uppercase"
                  style={{ letterSpacing: "0.1em", color: "var(--oo-muted)" }}
                >
                  BODS 0.4
                </span>
                <span
                  className="text-xs px-1.5 py-0.5 rounded"
                  style={{ background: "rgba(61,48,212,0.1)", color: "var(--oo-blue)" }}
                >
                  Mapped
                </span>
                <DownloadButton onClick={() => downloadJson(bodsData, bodsFilename)} label="BODS data" />
              </div>
              <pre
                className="text-xs p-3 overflow-auto max-h-80 font-mono"
                style={{ background: "var(--oo-bg)", borderRadius: 8, border: "1px solid var(--oo-rule)" }}
              >
                {bodsData}
              </pre>
            </div>
          </div>
        )}

        {view === "original" && (
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span
                className="text-xs font-semibold uppercase"
                style={{ letterSpacing: "0.1em", color: "var(--oo-muted)" }}
              >
                {originalFormat}
              </span>
              <DownloadButton onClick={() => downloadJson(originalJson, originalFilename)} label="original data" />
            </div>
            <pre
              className="text-xs p-3 overflow-auto max-h-96 font-mono"
              style={{ background: "var(--oo-bg)", borderRadius: 8, border: "1px solid var(--oo-rule)" }}
            >
              {originalJson}
            </pre>
          </div>
        )}

        {view === "bods" && (
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span
                className="text-xs font-semibold uppercase"
                style={{ letterSpacing: "0.1em", color: "var(--oo-muted)" }}
              >
                BODS 0.4
              </span>
              <DownloadButton onClick={() => downloadJson(bodsData, bodsFilename)} label="BODS data" />
            </div>
            <pre
              className="text-xs p-3 overflow-auto max-h-96 font-mono"
              style={{ background: "var(--oo-bg)", borderRadius: 8, border: "1px solid var(--oo-rule)" }}
            >
              {bodsData}
            </pre>
          </div>
        )}

        <div
          className="mt-3 p-3"
          style={{
            background: "rgba(61,48,212,0.04)",
            borderRadius: 8,
            border: "1px solid rgba(61,48,212,0.12)",
          }}
        >
          <p className="text-xs" style={{ color: "var(--oo-muted)", lineHeight: 1.7 }}>
            <strong style={{ color: "var(--oo-blue)" }}>Why standardise?</strong> By
            mapping national data formats to BODS, beneficial ownership
            information becomes interoperable across borders. This enables
            cross-referencing ownership structures internationally and supports
            anti-corruption and anti-money-laundering efforts.{" "}
            <a
              href="https://standard.openownership.org/en/0.4.0/"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:underline font-mono"
              style={{ color: "var(--oo-blue)", fontSize: 11 }}
            >
              Learn more about BODS &rarr;
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}
