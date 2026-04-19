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

  useEffect(() => {
    fetchExamples().then(setExamples).catch(() => {});
  }, []);

  const handleValidateJson = async (data: any) => {
    setIsLoading(true);
    setError("");
    setResults(null);
    setOriginalData(null);
    setOriginalFormat("");
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
