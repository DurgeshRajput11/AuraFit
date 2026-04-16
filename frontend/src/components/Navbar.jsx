import { Sparkles } from "lucide-react";

export default function Navbar() {
  return (
    <nav
      data-testid="navbar"
      className="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-[#05050A]/60 border-b border-white/5"
    >
      <div className="max-w-7xl mx-auto px-6 md:px-12 h-16 flex items-center justify-between">
        <a
          href="/"
          data-testid="navbar-logo"
          className="flex items-center gap-2.5 group"
        >
          <Sparkles className="w-5 h-5 text-[#4F46E5] transition-transform duration-300 group-hover:rotate-12" />
          <span className="font-heading text-xl tracking-tight text-[#F8FAFC] font-semibold">
            AuraFit
          </span>
        </a>
        <p className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8] hidden sm:block">
          Your Outfit Decision Engine
        </p>
      </div>
    </nav>
  );
}
