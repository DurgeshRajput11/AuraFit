import { ChevronDown } from "lucide-react";

const HERO_BG = "https://static.prod-images.emergentagent.com/jobs/cd80d8a0-deaa-45f2-9fcf-5661d52d51cb/images/fbe65fd2654d110653c9497da66e98ffa068328c347d9fa182ae52b52098eb15.png";

export default function HeroSection({ onGetStarted }) {
  return (
    <section
      data-testid="hero-section"
      className="relative w-full min-h-screen flex items-center justify-center overflow-hidden"
    >
      {/* Background Image */}
      <div className="absolute inset-0">
        <img
          src={HERO_BG}
          alt=""
          className="w-full h-full object-cover"
          loading="eager"
        />
        <div className="absolute inset-0 bg-[#05050A]/65" />
      </div>

      {/* Content */}
      <div className="relative z-10 text-center px-6 max-w-3xl mx-auto animate-fade-in-up">
        <p className="text-sm md:text-base uppercase tracking-[0.3em] font-body font-semibold text-[#4F46E5] opacity-90 mb-6">
           Stop Overthinking. Start Wearing.
         </p>
        <h1 className="font-heading text-5xl md:text-6xl lg:text-7xl tracking-tighter text-[#F8FAFC] leading-[1.05] mb-6">
          Your Perfect Outfit,
          <br />
          <span className="italic text-[#6366F1]">In Seconds</span>
        </h1>
        <p className="font-body text-base md:text-lg text-[#94A3B8] leading-relaxed max-w-xl mx-auto mb-10">
          Get 2-3 curated outfit recommendations based on your occasion, style, and season. No endless scrolling. Just confident decisions.
        </p>
        <button
          data-testid="hero-cta-button"
          onClick={onGetStarted}
          className="inline-flex items-center gap-2 px-8 py-3.5 rounded-full bg-[#4F46E5] hover:bg-[#6366F1] text-white font-body font-semibold text-sm tracking-wide transition-all duration-300 glow-primary hover:scale-105"
        >
          Find My Look
          <ChevronDown className="w-4 h-4" />
        </button>
      </div>

      {/* Bottom fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-[#05050A] to-transparent" />
    </section>
  );
}
