import { useState, useRef } from "react";

interface Props {
  onValidateJson: (data: any) => void;
  onValidateFile: (file: File) => void;
  onValidateUrl: (url: string) => void;
  isLoading: boolean;
  jsonValue: string;
  onJsonChange: (value: string) => void;
}

type Tab = "paste" | "upload" | "url";

export default function InputPanel({
  onValidateJson,
  onValidateFile,
  onValidateUrl,
  isLoading,
  jsonValue,
  onJsonChange,
}: Props) {
  const [tab, setTab] = useState<Tab>("paste");
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState("");
  const [parseError, setParseError] = useState("");
  const fileRef = useRef<HTMLInputElement>(null);

  const handlePasteValidate = () => {
    setParseError("");
    try {
      const parsed = JSON.parse(jsonValue);
      onValidateJson(parsed);
    } catch {
      setParseError("Invalid JSON. Please check your syntax.");
    }
  };

  const handleFileValidate = () => {
    if (file) onValidateFile(file);
  };

  const handleUrlValidate = () => {
    if (url.trim()) onValidateUrl(url.trim());
  };

  const tabClass = (t: Tab) =>
    `px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${
      tab === t
        ? "bg-white text-[#652eb1] border border-b-0 border-gray-200"
        : "text-gray-500 hover:text-gray-700 hover:bg-gray-50"
    }`;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200">
      <div className="flex gap-1 px-4 pt-4 border-b border-gray-200">
        <button className={tabClass("paste")} onClick={() => setTab("paste")}>
          Paste JSON
        </button>
        <button className={tabClass("upload")} onClick={() => setTab("upload")}>
          Upload File
        </button>
        <button className={tabClass("url")} onClick={() => setTab("url")}>
          Fetch URL
        </button>
      </div>

      <div className="p-4">
        {tab === "paste" && (
          <div>
            <textarea
              className="w-full h-80 font-mono text-sm p-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-[#652eb1] focus:border-transparent resize-y bg-gray-50"
              placeholder='Paste your BODS JSON data here...&#10;&#10;Example: [{"statementId": "...", "recordType": "entity", ...}]'
              value={jsonValue}
              onChange={(e) => {
                onJsonChange(e.target.value);
                setParseError("");
              }}
            />
            {parseError && (
              <p className="text-red-600 text-sm mt-1">{parseError}</p>
            )}
            <button
              onClick={handlePasteValidate}
              disabled={isLoading || !jsonValue.trim()}
              className="mt-3 px-6 py-2.5 bg-[#652eb1] text-white rounded-lg font-medium hover:bg-[#5425a0] disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? "Validating..." : "Validate"}
            </button>
          </div>
        )}

        {tab === "upload" && (
          <div>
            <div
              className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-[#652eb1] transition-colors cursor-pointer"
              onClick={() => fileRef.current?.click()}
              onDragOver={(e) => e.preventDefault()}
              onDrop={(e) => {
                e.preventDefault();
                const f = e.dataTransfer.files[0];
                if (f) setFile(f);
              }}
            >
              <input
                ref={fileRef}
                type="file"
                accept=".json"
                className="hidden"
                onChange={(e) => setFile(e.target.files?.[0] || null)}
              />
              {file ? (
                <div>
                  <p className="text-gray-800 font-medium">{file.name}</p>
                  <p className="text-gray-500 text-sm mt-1">
                    {(file.size / 1024).toFixed(1)} KB
                  </p>
                </div>
              ) : (
                <div>
                  <p className="text-gray-500">
                    Drop a .json file here or click to browse
                  </p>
                  <p className="text-gray-400 text-sm mt-1">Maximum 10MB</p>
                </div>
              )}
            </div>
            <button
              onClick={handleFileValidate}
              disabled={isLoading || !file}
              className="mt-3 px-6 py-2.5 bg-[#652eb1] text-white rounded-lg font-medium hover:bg-[#5425a0] disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? "Validating..." : "Validate"}
            </button>
          </div>
        )}

        {tab === "url" && (
          <div>
            <input
              type="url"
              className="w-full p-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-[#652eb1] focus:border-transparent bg-gray-50"
              placeholder="https://example.com/bods-data.json"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              onKeyDown={(e) =>
                e.key === "Enter" && url.trim() && handleUrlValidate()
              }
            />
            <button
              onClick={handleUrlValidate}
              disabled={isLoading || !url.trim()}
              className="mt-3 px-6 py-2.5 bg-[#652eb1] text-white rounded-lg font-medium hover:bg-[#5425a0] disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? "Validating..." : "Validate"}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
