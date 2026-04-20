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
    <div
      className="bg-white shadow-sm p-6"
      style={{ borderRadius: 10, border: "1px solid var(--oo-rule)" }}
    >
      <div
        className="text-[10px] font-semibold uppercase mb-5 pb-2.5"
        style={{
          letterSpacing: "0.12em",
          color: "var(--oo-muted)",
          borderBottom: "1px solid var(--oo-rule)",
        }}
      >
        Example Datasets
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        {examples.map((ex) => (
          <button
            key={ex.id}
            onClick={() => onLoadExample(ex.id)}
            disabled={isLoading}
            className="text-left p-4 transition-all disabled:opacity-50 group"
            style={{
              borderRadius: 10,
              border: "1px solid var(--oo-rule)",
              background: "#fff",
            }}
            onMouseEnter={(e) => {
              (e.currentTarget as HTMLElement).style.boxShadow = "0 8px 32px rgba(61,48,212,0.10)";
            }}
            onMouseLeave={(e) => {
              (e.currentTarget as HTMLElement).style.boxShadow = "none";
            }}
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
                className="ml-auto px-2 py-0.5 text-xs font-medium"
                style={{
                  borderRadius: 20,
                  background: ex.valid ? "#e8fbe8" : "#fde8e8",
                  color: ex.valid ? "#1a7a1a" : "#b91c1c",
                  fontFamily: "var(--mono, 'DM Mono', monospace)",
                }}
              >
                {ex.valid ? "Valid" : "Has Errors"}
              </span>
            </div>
            <p
              className="font-bold text-sm mb-1 transition-colors"
              style={{ fontFamily: "'Bitter', Georgia, serif", color: "var(--oo-navy)" }}
            >
              {ex.title}
            </p>
            <p className="text-xs" style={{ color: "var(--oo-muted)", lineHeight: 1.7 }}>
              {ex.description}
            </p>
            {ex.has_original && (
              <p
                className="text-xs mt-1.5 font-medium"
                style={{ color: "var(--oo-blue)", fontFamily: "'DM Mono', monospace", fontSize: 11 }}
              >
                Includes original {ex.original_format} data for comparison
              </p>
            )}
          </button>
        ))}
      </div>
    </div>
  );
}
