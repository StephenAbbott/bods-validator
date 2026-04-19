import { useRef, useEffect, useState } from "react";

declare global {
  interface Window {
    BODSDagre?: {
      draw: (config: any) => void;
    };
    d3?: any;
  }
}

interface Props {
  data: any;
}

function loadScript(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (document.querySelector(`script[src="${src}"]`)) {
      resolve();
      return;
    }
    const script = document.createElement("script");
    script.src = src;
    script.onload = () => resolve();
    script.onerror = () => reject(new Error(`Failed to load ${src}`));
    document.head.appendChild(script);
  });
}

// Arrow marker definitions that bods-dagre creates but may get lost
const ARROW_MARKERS = [
  { id: "arrow-control-Half", d: "M 0 0 L 10 5 L 0 5 z", fill: "#349aee", refY: 3.8 },
  { id: "arrow-control-Full", d: "M 0 0 L 10 5 L 0 10 z", fill: "#349aee", refY: 5 },
  { id: "arrow-control-blackHalf", d: "M 0 0 L 10 5 L 0 10 z", fill: "#000", refY: 5 },
  { id: "arrow-control-blackFull", d: "M 0 0 L 10 5 L 0 10 z", fill: "#000", refY: 5 },
  { id: "arrow-own-Half", d: "M 0 10 L 10 5 L 0 5 z", fill: "#652eb1", refY: 6.1 },
  { id: "arrow-own-Full", d: "M 0 10 L 10 5 L 0 0 z", fill: "#652eb1", refY: 5 },
  { id: "arrow-own-blackHalf", d: "M 0 10 L 10 5 L 0 5 z", fill: "#000", refY: 6.1 },
  { id: "arrow-own-blackFull", d: "M 0 10 L 10 5 L 0 0 z", fill: "#000", refY: 5 },
  { id: "arrow-unknown-blackHalf", d: "M 0 10 L 10 5 L 0 5 z", fill: "#000", refY: 6.1 },
  { id: "arrow-unknown-blackFull", d: "M 0 10 L 10 5 L 0 0 z", fill: "#000", refY: 5 },
];

function ensureArrowMarkers(svg: SVGSVGElement) {
  let defs = svg.querySelector("defs");
  if (!defs) {
    defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
    svg.insertBefore(defs, svg.firstChild);
  }

  for (const marker of ARROW_MARKERS) {
    if (!svg.querySelector(`#${marker.id}`)) {
      const m = document.createElementNS("http://www.w3.org/2000/svg", "marker");
      m.setAttribute("id", marker.id);
      m.setAttribute("viewBox", "0 0 10 10");
      m.setAttribute("refX", "8");
      m.setAttribute("refY", String(marker.refY));
      m.setAttribute("markerUnits", "userSpaceOnUse");
      m.setAttribute("markerWidth", "40");
      m.setAttribute("markerHeight", "40");
      m.setAttribute("orient", "auto-start-reverse");

      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.setAttribute("d", marker.d);
      path.setAttribute("stroke", "none");
      path.setAttribute("fill", marker.fill);
      m.appendChild(path);
      defs.appendChild(m);
    }
  }
}

function fixEdges(svg: SVGSVGElement) {
  // Force all edgePaths to be visible (d3 transitions may not complete)
  svg.querySelectorAll("g.edgePath").forEach((edge) => {
    (edge as SVGGElement).style.opacity = "1";
  });

  // Fix paths that start with NaN by hiding them (they are duplicate overlays)
  svg.querySelectorAll("g.edgePath path").forEach((path) => {
    const d = path.getAttribute("d") || "";
    if (d.includes("NaN")) {
      // Try to reconstruct from the base edge path in the same group
      const parent = path.closest("g.edgePath");
      if (parent) {
        const basePath = parent.querySelector("path:not([id])");
        if (basePath && basePath !== path) {
          const baseD = basePath.getAttribute("d") || "";
          if (!baseD.includes("NaN")) {
            path.setAttribute("d", baseD);
            return;
          }
        }
      }
      // If we can't fix it, hide just this path element
      (path as SVGPathElement).style.display = "none";
    }
  });
}

function fixTransform(svg: SVGSVGElement, container: HTMLDivElement) {
  const rootG = svg.querySelector("g");
  if (!rootG) return;

  const transform = rootG.getAttribute("transform") || "";
  if (!transform.includes("scale(0)")) return;

  // Calculate proper viewBox from node positions
  const nodes = svg.querySelectorAll("g.node");
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  nodes.forEach((n) => {
    const t = n.getAttribute("transform") || "";
    const m = t.match(/translate\(([\d.-]+)\s*,\s*([\d.-]+)\)/);
    if (m) {
      const x = parseFloat(m[1]), y = parseFloat(m[2]);
      minX = Math.min(minX, x - 100);
      minY = Math.min(minY, y - 80);
      maxX = Math.max(maxX, x + 100);
      maxY = Math.max(maxY, y + 80);
    }
  });
  const w = maxX - minX || 400;
  const h = maxY - minY || 300;
  const containerW = container.offsetWidth;
  const scale = Math.min(containerW / w, 500 / h, 1.2);
  const tx = (containerW - w * scale) / 2 - minX * scale;
  const ty = 30 - minY * scale;
  rootG.setAttribute("transform", `translate(${tx},${ty}) scale(${scale})`);
  svg.setAttribute("width", String(containerW));
  svg.setAttribute("height", String(h * scale + 60));
  container.style.minHeight = `${h * scale + 60}px`;
}

export default function VisualisationPanel({ data }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [error, setError] = useState("");
  const [rendered, setRendered] = useState(false);
  const [loading, setLoading] = useState(false);
  const lastWidthRef = useRef<number>(0);

  useEffect(() => {
    setRendered(false);
    setError("");
  }, [data]);

  const drawGraph = (container: HTMLDivElement) => {
    container.innerHTML = "";
    container.style.minHeight = "400px";
    container.style.width = "100%";

    try {
      window.BODSDagre!.draw({
        data: data,
        selectedData: data,
        container: "#bods-viz-container",
        imagesPath: "/bods-images/",
        labelLimit: 30,
        rankDir: "LR",
        viewProperties: false,
        useTippy: false,
      });
    } catch {
      // The library may throw on optional UI features (properties panel);
      // the SVG graph itself renders successfully before this point.
    }

    const svg = container.querySelector("svg");
    if (!svg || svg.querySelectorAll("g.node").length === 0) {
      throw new Error("No ownership graph could be generated from this data.");
    }

    const applyFixes = () => {
      const svg = container.querySelector("svg");
      if (!svg) return;
      ensureArrowMarkers(svg);
      fixEdges(svg);
      fixTransform(svg, container);
    };

    applyFixes();
    setTimeout(applyFixes, 300);
    setTimeout(applyFixes, 600);
  };

  // Re-render on container resize
  useEffect(() => {
    if (!rendered || !containerRef.current) return;

    const observer = new ResizeObserver((entries) => {
      const entry = entries[0];
      if (!entry || !containerRef.current || !window.BODSDagre) return;
      const newWidth = Math.round(entry.contentRect.width);
      // Only re-draw if width changed significantly (> 50px)
      if (Math.abs(newWidth - lastWidthRef.current) > 50) {
        lastWidthRef.current = newWidth;
        try {
          drawGraph(containerRef.current);
        } catch {
          // ignore resize draw errors
        }
      }
    });

    observer.observe(containerRef.current);
    return () => observer.disconnect();
  }, [rendered, data]);

  const handleRender = async () => {
    if (!containerRef.current) return;
    setError("");
    setLoading(true);

    try {
      await loadScript(
        "/lib/bods-dagre.js"
      );

      if (!window.BODSDagre) {
        throw new Error("BODSDagre library not available after loading");
      }

      lastWidthRef.current = containerRef.current.offsetWidth;
      drawGraph(containerRef.current);
      setRendered(true);
    } catch (e: any) {
      setError(e.message || "Failed to render visualisation");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200 bg-gradient-to-r from-[#652eb1]/5 to-[#349aee]/5">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex gap-1.5">
              <img src="/bods-images/bovs-person.svg" alt="" className="w-5 h-5" />
              <svg width="20" height="12" viewBox="0 0 20 12" className="self-center">
                <defs>
                  <marker id="arr" markerWidth="6" markerHeight="4" refX="5" refY="2" orient="auto">
                    <path d="M0,0 L6,2 L0,4" fill="#652eb1" />
                  </marker>
                </defs>
                <line x1="0" y1="6" x2="14" y2="6" stroke="#652eb1" strokeWidth="2" markerEnd="url(#arr)" />
              </svg>
              <img src="/bods-images/bovs-organisation.svg" alt="" className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-semibold text-gray-900">Ownership Visualisation</h3>
              <p className="text-xs text-gray-500">
                Powered by the{" "}
                <a
                  href="https://github.com/openownership/visualisation-tool"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#652eb1] hover:underline"
                >
                  BODS Visualisation Library
                </a>
              </p>
            </div>
          </div>
          {!rendered && (
            <button
              onClick={handleRender}
              disabled={loading}
              className="px-4 py-2 bg-[#652eb1] text-white rounded-lg text-sm font-medium hover:bg-[#5425a0] transition-colors flex items-center gap-2 disabled:opacity-50"
            >
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <circle cx="4" cy="4" r="2.5" stroke="currentColor" strokeWidth="1.5" />
                <circle cx="12" cy="4" r="2.5" stroke="currentColor" strokeWidth="1.5" />
                <circle cx="8" cy="12" r="2.5" stroke="currentColor" strokeWidth="1.5" />
                <line x1="4" y1="6.5" x2="8" y2="9.5" stroke="currentColor" strokeWidth="1.5" />
                <line x1="12" y1="6.5" x2="8" y2="9.5" stroke="currentColor" strokeWidth="1.5" />
              </svg>
              {loading ? "Rendering..." : "Visualise Ownership"}
            </button>
          )}
        </div>
      </div>

      {error && (
        <div className="p-3 bg-red-50 text-red-700 text-sm border-b border-red-200">
          {error}
        </div>
      )}

      <div
        id="bods-viz-container"
        ref={containerRef}
        className="min-h-[100px]"
        style={rendered ? { minHeight: "400px" } : {}}
      />

      {!rendered && !error && !loading && (
        <div className="p-6 text-center">
          <div className="flex justify-center gap-2 mb-3 opacity-30">
            <img src="/bods-images/bovs-person.svg" alt="" className="w-10 h-10" />
            <img src="/bods-images/bovs-organisation.svg" alt="" className="w-10 h-10" />
            <img src="/bods-images/bovs-arrangement.svg" alt="" className="w-10 h-10" />
          </div>
          <p className="text-gray-500 text-sm">
            Your validated BODS data can be visualised as an interactive ownership diagram.
          </p>
          <p className="text-gray-400 text-xs mt-1">
            Uses the{" "}
            <a
              href="https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[#652eb1] hover:underline"
            >
              Beneficial Ownership Visualisation System (BOVS)
            </a>{" "}
            icons and conventions.
            <span className="inline-block ml-1">
              <span className="text-[#652eb1]">Purple</span> = ownership,{" "}
              <span className="text-[#349aee]">cyan</span> = control.
            </span>
          </p>
        </div>
      )}
    </div>
  );
}
