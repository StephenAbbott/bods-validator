import type { ExampleSummary } from "../types";

interface Props {
  examples: ExampleSummary[];
  onLoadExample: (id: string) => void;
  isLoading: boolean;
}

const FLAG_EMOJI: Record<string, string> = {
  GB: "\uD83C\uDDEC\uD83C\uDDE7",
  ID: "\uD83C\uDDEE\uD83C\uDDE9",
  DK: "\uD83C\uDDE9\uD83C\uDDF0",
  FR: "\uD83C\uDDEB\uD83C\uDDF7",
  NO: "\uD83C\uDDF3\uD83C\uDDF4",
};

export default function ExamplesPanel({ examples, onLoadExample, isLoading }: Props) {
  if (examples.length === 0) return null;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-4">
      <h3 className="font-semibold text-gray-900 mb-3">Example Datasets</h3>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {examples.map((ex) => (
          <button
            key={ex.id}
            onClick={() => onLoadExample(ex.id)}
            disabled={isLoading}
            className="text-left p-3 rounded-lg border border-gray-200 hover:border-[#652eb1] hover:bg-purple-50 transition-colors disabled:opacity-50 group"
          >
            <div className="flex items-center gap-2 mb-2">
              {ex.icon && (
                <img
                  src={`/bods-images/${ex.icon}.svg`}
                  alt=""
                  className="w-6 h-6"
                />
              )}
              {ex.country && FLAG_EMOJI[ex.country] && (
                <span className="text-lg">{FLAG_EMOJI[ex.country]}</span>
              )}
              <span
                className={`ml-auto px-2 py-0.5 text-xs rounded-full font-medium ${
                  ex.valid
                    ? "bg-green-100 text-green-700"
                    : "bg-red-100 text-red-700"
                }`}
              >
                {ex.valid ? "Valid" : "Has Errors"}
              </span>
            </div>
            <p className="font-medium text-sm text-gray-900 group-hover:text-[#652eb1] transition-colors">
              {ex.title}
            </p>
            <p className="text-xs text-gray-500 mt-1">{ex.description}</p>
            {ex.has_original && (
              <p className="text-xs text-[#349aee] mt-1 font-medium">
                Includes original {ex.original_format} data for comparison
              </p>
            )}
          </button>
        ))}
      </div>
    </div>
  );
}
