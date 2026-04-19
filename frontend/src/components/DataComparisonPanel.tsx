import { useState } from "react";

interface Props {
  originalData: any;
  originalFormat: string;
  bodsData: string;
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
      className="inline-flex items-center gap-1 text-xs text-gray-400 hover:text-[#652eb1] transition-colors"
    >
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
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
}: Props) {
  const [view, setView] = useState<"side-by-side" | "original" | "bods">(
    "side-by-side"
  );

  const originalJson = JSON.stringify(originalData, null, 2);

  const tabClass = (v: string) =>
    `px-3 py-1.5 text-xs font-medium rounded transition-colors ${
      view === v
        ? "bg-[#652eb1] text-white"
        : "text-gray-500 hover:text-gray-700 hover:bg-gray-100"
    }`;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              fill="none"
              className="text-[#349aee]"
            >
              <rect
                x="1"
                y="2"
                width="7"
                height="16"
                rx="1"
                stroke="currentColor"
                strokeWidth="1.5"
              />
              <rect
                x="12"
                y="2"
                width="7"
                height="16"
                rx="1"
                stroke="currentColor"
                strokeWidth="1.5"
              />
              <path
                d="M8 10h4"
                stroke="currentColor"
                strokeWidth="1.5"
                strokeDasharray="2 2"
              />
            </svg>
            <h3 className="font-semibold text-gray-900">
              Data Mapping: {originalFormat} &rarr; BODS 0.4
            </h3>
          </div>
          <div className="flex gap-1">
            <button className={tabClass("side-by-side")} onClick={() => setView("side-by-side")}>
              Side by Side
            </button>
            <button className={tabClass("original")} onClick={() => setView("original")}>
              {originalFormat}
            </button>
            <button className={tabClass("bods")} onClick={() => setView("bods")}>
              BODS 0.4
            </button>
          </div>
        </div>
        <p className="text-xs text-gray-500 mt-2">
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
                <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  {originalFormat}
                </span>
                <span className="text-xs bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded">
                  Original
                </span>
                <DownloadButton onClick={() => downloadJson(originalJson, "original-data.json")} label="original data" />
              </div>
              <pre className="text-xs bg-gray-50 p-3 rounded-lg border border-gray-200 overflow-auto max-h-80 font-mono">
                {originalJson}
              </pre>
            </div>
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
                  BODS 0.4
                </span>
                <span className="text-xs bg-[#652eb1]/10 text-[#652eb1] px-1.5 py-0.5 rounded">
                  Mapped
                </span>
                <DownloadButton onClick={() => downloadJson(bodsData, "bods-0.4.json")} label="BODS data" />
              </div>
              <pre className="text-xs bg-gray-50 p-3 rounded-lg border border-gray-200 overflow-auto max-h-80 font-mono">
                {bodsData}
              </pre>
            </div>
          </div>
        )}

        {view === "original" && (
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">{originalFormat}</span>
              <DownloadButton onClick={() => downloadJson(originalJson, "original-data.json")} label="original data" />
            </div>
            <pre className="text-xs bg-gray-50 p-3 rounded-lg border border-gray-200 overflow-auto max-h-96 font-mono">
              {originalJson}
            </pre>
          </div>
        )}

        {view === "bods" && (
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">BODS 0.4</span>
              <DownloadButton onClick={() => downloadJson(bodsData, "bods-0.4.json")} label="BODS data" />
            </div>
            <pre className="text-xs bg-gray-50 p-3 rounded-lg border border-gray-200 overflow-auto max-h-96 font-mono">
              {bodsData}
            </pre>
          </div>
        )}

        <div className="mt-3 p-3 bg-[#349aee]/5 rounded-lg border border-[#349aee]/20">
          <p className="text-xs text-gray-600">
            <strong className="text-[#349aee]">Why standardise?</strong> By
            mapping national data formats to BODS, beneficial ownership
            information becomes interoperable across borders. This enables
            cross-referencing ownership structures internationally and supports
            anti-corruption and anti-money-laundering efforts.{" "}
            <a
              href="https://standard.openownership.org/en/0.4.0/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[#652eb1] hover:underline"
            >
              Learn more about BODS &rarr;
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}
