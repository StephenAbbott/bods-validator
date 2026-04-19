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
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-[#1a1a2e] text-white">
        <div className="max-w-5xl mx-auto px-4 py-6">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-3">
              <img
                src="/bods-images/bovs-organisation.svg"
                alt=""
                className="w-10 h-10 invert brightness-200"
              />
              <div>
                <h1 className="text-2xl font-bold tracking-tight">
                  BODS Validator
                </h1>
                <p className="text-gray-300 text-sm mt-0.5">
                  Validate & visualise Beneficial Ownership Data
                </p>
              </div>
            </div>
            <div className="ml-auto flex items-center gap-3">
              <a
                href="https://standard.openownership.org/en/0.4.0/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-gray-300 hover:text-white transition-colors"
              >
                BODS 0.4.0 Standard
              </a>
              <span className="text-gray-600">|</span>
              <a
                href="https://www.openownership.org/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-gray-300 hover:text-white transition-colors"
              >
                Open Ownership
              </a>
            </div>
          </div>
        </div>
        {/* Purple/cyan accent bar */}
        <div className="h-1 flex">
          <div className="flex-1 bg-[#652eb1]" />
          <div className="flex-1 bg-[#349aee]" />
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-5xl mx-auto px-4 py-6 space-y-6">
        {/* Intro banner */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-5">
          <div className="flex flex-col md:flex-row gap-4 items-start">
            <div className="flex gap-3 shrink-0">
              <img src="/bods-images/bovs-person.svg" alt="" className="w-8 h-8" />
              <img src="/bods-images/bovs-organisation.svg" alt="" className="w-8 h-8" />
              <img src="/bods-images/bovs-arrangement.svg" alt="" className="w-8 h-8" />
            </div>
            <div>
              <p className="text-gray-700 text-sm">
                The{" "}
                <a
                  href="https://standard.openownership.org/en/0.4.0/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#652eb1] font-medium hover:underline"
                >
                  Beneficial Ownership Data Standard (BODS)
                </a>{" "}
                provides a structured format for publishing information about
                who owns and controls companies. Submit your JSON data to
                validate it against the schema, get actionable guidance, and
                visualise ownership structures using the{" "}
                <a
                  href="https://www.openownership.org/en/publications/beneficial-ownership-data-standard-visualisation-library/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#349aee] font-medium hover:underline"
                >
                  BODS Visualisation Library
                </a>
                .
              </p>
            </div>
          </div>
        </div>

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
          <div className="bg-red-50 border border-red-200 rounded-xl p-4">
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {results && <ResultsPanel results={results} />}

        {results && (results.valid || results.schema_valid) && validatedData && (
          <VisualisationPanel data={validatedData} />
        )}
      </main>

      {/* Footer */}
      <footer className="bg-[#1a1a2e] text-gray-400 mt-12">
        <div className="h-1 flex">
          <div className="flex-1 bg-[#652eb1]" />
          <div className="flex-1 bg-[#349aee]" />
        </div>
        <div className="max-w-5xl mx-auto px-4 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <div className="flex items-center gap-3">
              <img
                src="/bods-images/bovs-organisation.svg"
                alt=""
                className="w-6 h-6 invert brightness-200"
              />
              <p className="text-sm">
                Built on the{" "}
                <a
                  href="https://standard.openownership.org/en/0.4.0/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#c084fc] hover:text-white transition-colors"
                >
                  Beneficial Ownership Data Standard
                </a>{" "}
                by{" "}
                <a
                  href="https://www.openownership.org/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#c084fc] hover:text-white transition-colors"
                >
                  Open Ownership
                </a>
              </p>
            </div>
            <div className="flex flex-col sm:flex-row flex-wrap justify-center items-center gap-2 sm:gap-4 text-sm">
              <a
                href="https://github.com/StephenAbbott/bods-validator"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-white transition-colors flex items-center gap-1"
              >
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                Source Code
              </a>
              <a
                href="https://github.com/openownership/lib-cove-bods"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-white transition-colors"
              >
                lib-cove-bods
              </a>
              <a
                href="https://github.com/openownership/visualisation-tool"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-white transition-colors"
              >
                Visualisation Library
              </a>
              <a
                href="https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-white transition-colors"
              >
                BOVS Icons
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
