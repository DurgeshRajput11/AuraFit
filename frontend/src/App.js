import { useState, useEffect, useCallback, useRef } from "react";
import "@/App.css";
import axios from "axios";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import OccasionSelector from "./components/OccasionSelector";
import FilterBar from "./components/FilterBar";
import OutfitGrid from "./components/OutfitGrid";
import OutfitDetail from "./components/OutfitDetail";
import EmptyState from "./components/EmptyState";
import { Loader2 } from "lucide-react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;
console.log("BACKEND:", BACKEND_URL);
console.log("API:", API);

function App() {
  const [occasion, setOccasion] = useState("college");
  const [gender, setGender] = useState("men");
  const [season, setSeason] = useState("all");
  const [style, setStyle] = useState("all");
  const [outfits, setOutfits] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedOutfit, setSelectedOutfit] = useState(null);
  const [detailOpen, setDetailOpen] = useState(false);
  const [stats, setStats] = useState(null);
  const resultsRef = useRef(null);

  const fetchOutfits = useCallback(async () => {
    setLoading(true);
    try {
      const params = { occasion, gender, limit: 3 };
      if (season && season !== "all") params.season = season;
      if (style && style !== "all") params.style = style;

      const res = await axios.get(`${API}/outfits`, { params });
      setOutfits(res.data.outfits || []);
    } catch (err) {
      console.error("Failed to fetch outfits:", err);
      setOutfits([]);
    } finally {
      setLoading(false);
    }
  }, [occasion, gender, season, style]);

  useEffect(() => {
    fetchOutfits();
  }, [fetchOutfits]);

  useEffect(() => {
    axios.get(`${API}/stats`).then((res) => setStats(res.data)).catch(() => {});
  }, []);

  const handleGetStarted = () => {
    resultsRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleSelectOutfit = (outfit) => {
    setSelectedOutfit(outfit);
    setDetailOpen(true);
  };

  return (
    <div className="noise min-h-screen bg-[#05050A]">
      <Navbar />
      <HeroSection onGetStarted={handleGetStarted} />

      {/* Main Content */}
      <main
        ref={resultsRef}
        className="relative z-10 max-w-7xl mx-auto px-6 md:px-12 pt-20 pb-32"
      >
        {/* Section Header */}
        <div className="mb-12">
          <p className="text-xs uppercase tracking-[0.25em] font-body font-semibold text-[#4F46E5] mb-3">
            Curated For You
          </p>
          <h2 className="font-heading text-3xl md:text-4xl tracking-tight text-[#F8FAFC] mb-2">
            Pick Your Vibe
          </h2>
          <p className="font-body text-base text-[#94A3B8] max-w-lg">
            Select an occasion and refine with your preferences. We will show you 2-3 ready-to-wear looks.
          </p>
        </div>

        {/* Filters Section */}
        <div data-testid="filters-section" className="space-y-6 mb-12">
          <OccasionSelector selected={occasion} onSelect={setOccasion} />
          <FilterBar
            gender={gender}
            season={season}
            style={style}
            onGenderChange={setGender}
            onSeasonChange={setSeason}
            onStyleChange={(v) => setStyle(v === "all" ? "all" : v)}
          />
        </div>

        {/* Results */}
        <div data-testid="results-section">
          {loading ? (
            <div className="flex items-center justify-center py-20">
              <Loader2 className="w-8 h-8 text-[#4F46E5] animate-spin" />
            </div>
          ) : outfits.length > 0 ? (
            <>
              <p className="font-body text-sm text-[#94A3B8] mb-6">
                Showing <span className="text-[#F8FAFC] font-medium">{outfits.length}</span> curated{" "}
                {outfits.length === 1 ? "look" : "looks"}
              </p>
              <OutfitGrid outfits={outfits} onSelect={handleSelectOutfit} />
            </>
          ) : (
            <EmptyState />
          )}
        </div>

        {/* Stats Footer */}
        {stats && (
          <div
            data-testid="stats-section"
            className="mt-24 pt-12 border-t border-white/5 flex flex-wrap gap-8 justify-center"
          >
            <div className="text-center">
              <p className="font-heading text-3xl text-[#F8FAFC]">{stats.total_outfits}</p>
              <p className="font-body text-xs uppercase tracking-[0.15em] text-[#94A3B8] mt-1">
                Total Looks
              </p>
            </div>
            {stats.by_occasion &&
              Object.entries(stats.by_occasion).map(([occ, count]) => (
                <div key={occ} className="text-center">
                  <p className="font-heading text-3xl text-[#F8FAFC]">{count}</p>
                  <p className="font-body text-xs uppercase tracking-[0.15em] text-[#94A3B8] mt-1 capitalize">
                    {occ}
                  </p>
                </div>
              ))}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-white/5 py-8">
        <div className="max-w-7xl mx-auto px-6 md:px-12 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="font-body text-xs text-[#94A3B8]">
            AuraFit &mdash; Your Outfit Decision Engine
          </p>
          <p className="font-body text-xs text-[#94A3B8]/50">
            Outfit decisions in under 10 seconds
          </p>
        </div>
      </footer>

      {/* Outfit Detail Modal */}
      <OutfitDetail
        outfit={selectedOutfit}
        open={detailOpen}
        onClose={setDetailOpen}
      />
    </div>
  );
}

export default App;
