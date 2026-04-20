import { useState, useEffect } from "react";
import InputPanel from "./components/InputPanel";
import ResultsPanel from "./components/ResultsPanel";
import ExamplesPanel from "./components/ExamplesPanel";
import VisualisationPanel from "./components/VisualisationPanel";
import DataComparisonPanel from "./components/DataComparisonPanel";
import {
  validateJson,
  validateFile,
  validateUrl,
  fetchExamples,
  fetchExample,
} from "./api";
import type { ValidationResult, ExampleSummary } from "./types";

const ICON_TYPES = [
  { src: "/bods-images/bovs-person.svg", label: "Person" },
  { src: "/bods-images/bovs-organisation.svg", label: "Organisation" },
  { src: "/bods-images/bovs-entity-unknown.svg", label: "Entity" },
  { src: "/bods-images/bovs-arrangement.svg", label: "Arrangement" },
  { src: "/bods-images/bovs-state.svg", label: "State" },
  { src: "/bods-images/bovs-statebody.svg", label: "SOE" },
  { src: "/bods-images/bovs-listed.svg", label: "Listed" },
  { src: "/bods-images/bovs-unknown.svg", label: "Unknown" },
];

function App() {
  const [results, setResults] = useState<ValidationResult | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [examples, setExamples] = useState<ExampleSummary[]>([]);
  const [jsonValue, setJsonValue] = useState("");
  const [validatedData, setValidatedData] = useState<any>(null);
  const [originalData, setOriginalData] = useState<any>(null);
  const [originalFormat, setOriginalFormat] = useState<string>("");
  const [exampleId, setExampleId] = useState<string>("");

  useEffect(() => {
    fetchExamples().then(setExamples).catch(() => {});
  }, []);

  const handleValidateJson = async (data: any) => {
    setIsLoading(true);
    setError("");
    setResults(null);
    setOriginalData(null);
    setOriginalFormat("");
    setExampleId("");
    try {
      const result = await validateJson(data);
      setResults(result);
      setValidatedData(data);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleValidateFile = async (file: File) => {
    setIsLoading(true);
    setError("");
    setResults(null);
    setOriginalData(null);
    setOriginalFormat("");
    setExampleId("");
    try {
      const result = await validateFile(file);
      setResults(result);
      const text = await file.text();
      setValidatedData(JSON.parse(text));
    } catch (e: any) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleValidateUrl = async (url: string) => {
    setIsLoading(true);
    setError("");
    setResults(null);
    setOriginalData(null);
    setOriginalFormat("");
    setExampleId("");
    try {
      const result = await validateUrl(url);
      setResults(result);
      setValidatedData(null);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleLoadExample = async (id: string) => {
    setIsLoading(true);
    setError("");
    try {
      const example = await fetchExample(id);
      const json = JSON.stringify(example.data, null, 2);
      setJsonValue(json);
      setResults(null);
      setValidatedData(null);
      setExampleId(id);
      if (example.original_data) {
        setOriginalData(example.original_data);
        setOriginalFormat(example.original_format || "Original");
      } else {
        setOriginalData(null);
        setOriginalFormat("");
      }
    } catch (e: any) {
      setError(e.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen" style={{ background: "var(--oo-bg)" }}>
      {/* Header */}
      <header
        className="text-white relative overflow-hidden"
        style={{ background: "var(--oo-navy)", padding: "48px 0 40px" }}
      >
        {/* Radial gradient overlay */}
        <div
          className="absolute pointer-events-none"
          style={{
            right: -80,
            top: -80,
            width: 500,
            height: 500,
            borderRadius: "50%",
            background: "radial-gradient(circle, rgba(61,48,212,0.28) 0%, transparent 70%)",
          }}
        />
        <div className="max-w-[1100px] mx-auto px-6 md:px-[60px] relative z-10">
          <div
            className="text-[11px] font-semibold uppercase mb-3"
            style={{ letterSpacing: "0.12em", color: "var(--oo-light)" }}
          >
            BODS Validator
          </div>
          <h1
            className="font-bold text-white"
            style={{ fontSize: "clamp(24px, 4vw, 38px)", lineHeight: 1.15 }}
          >
            Validate & visualise beneficial ownership data
          </h1>
          <p
            className="mt-3.5 max-w-[560px]"
            style={{ fontSize: 15, lineHeight: 1.65, color: "rgba(255,255,255,0.72)" }}
          >
            Submit your JSON data to validate it against the{" "}
            <a
              href="https://standard.openownership.org/en/0.4.0/"
              target="_blank"
              rel="noopener noreferrer"
              className="underline"
              style={{ color: "var(--oo-light)" }}
            >
              Beneficial Ownership Data Standard (BODS)
            </a>
            , get actionable guidance, and visualise ownership structures.
          </p>
          <div
            className="inline-flex items-center gap-1.5 mt-5"
            style={{
              padding: "6px 12px",
              borderRadius: 20,
              border: "1px solid rgba(220,238,255,0.35)",
              fontSize: 11,
              fontWeight: 500,
              color: "#dceeff",
              letterSpacing: "0.04em",
            }}
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <circle cx="12" cy="12" r="10" />
              <path d="M12 8v4m0 4h.01" />
            </svg>
            BODS 0.4.0 &middot; Open Ownership
          </div>
        </div>
      </header>

      {/* Icon strip */}
      <div
        className="flex items-center gap-8 overflow-x-auto"
        style={{ background: "var(--oo-burst)", padding: "20px 60px" }}
      >
        <span
          className="text-[10px] font-semibold uppercase shrink-0"
          style={{ letterSpacing: "0.1em", color: "rgba(255,255,255,0.5)" }}
        >
          Entity Types
        </span>
        <div className="flex gap-5 items-center flex-wrap">
          {ICON_TYPES.map((icon) => (
            <div key={icon.label} className="flex flex-col items-center gap-1">
              <img
                src={icon.src}
                alt={icon.label}
                className="w-10 h-10 invert brightness-200"
                style={{ objectFit: "contain" }}
              />
              <span
                className="text-[9px] font-medium whitespace-nowrap"
                style={{ color: "rgba(255,255,255,0.6)", letterSpacing: "0.04em" }}
              >
                {icon.label}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Main content */}
      <main className="max-w-[1100px] mx-auto px-6 md:px-[60px] py-12 space-y-6">
        <ExamplesPanel
          examples={examples}
          onLoadExample={handleLoadExample}
          isLoading={isLoading}
        />

        {originalData && (
          <DataComparisonPanel
            originalData={originalData}
            originalFormat={originalFormat}
            bodsData={jsonValue}
            exampleId={exampleId}
          />
        )}

        <InputPanel
          onValidateJson={handleValidateJson}
          onValidateFile={handleValidateFile}
          onValidateUrl={handleValidateUrl}
          isLoading={isLoading}
          jsonValue={jsonValue}
          onJsonChange={setJsonValue}
        />

        {error && (
          <div
            className="bg-red-50 p-4"
            style={{ border: "1px solid var(--oo-rule)", borderRadius: 10 }}
          >
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {results && <ResultsPanel results={results} />}

        {results && (results.valid || results.schema_valid) && validatedData && (
          <VisualisationPanel data={validatedData} />
        )}
      </main>

      {/* Footer — light style per design system */}
      <footer
        className="text-center"
        style={{
          padding: 32,
          fontSize: 12,
          color: "var(--oo-muted)",
          borderTop: "1px solid var(--oo-rule)",
        }}
      >
        Built on the{" "}
        <a
          href="https://standard.openownership.org/en/0.4.0/"
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: "var(--oo-blue)", textDecoration: "none" }}
        >
          Beneficial Ownership Data Standard
        </a>{" "}
        by{" "}
        <a
          href="https://www.openownership.org/"
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: "var(--oo-blue)", textDecoration: "none" }}
        >
          Open Ownership
        </a>
        {" "}&middot;{" "}
        <a
          href="https://github.com/StephenAbbott/bods-validator"
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: "var(--oo-blue)", textDecoration: "none" }}
        >
          Source Code
        </a>
        {" "}&middot;{" "}
        <a
          href="https://creativecommons.org/licenses/by/4.0/"
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: "var(--oo-blue)", textDecoration: "none" }}
        >
          CC BY 4.0
        </a>
      </footer>
    </div>
  );
}

export default App;
