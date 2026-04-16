import { GraduationCap, Coffee, Heart, Gem, PartyPopper, Briefcase } from "lucide-react";

const OCCASIONS = [
  { id: "college", label: "College", icon: GraduationCap },
  { id: "casual", label: "Casual", icon: Coffee },
  { id: "date", label: "Date", icon: Heart },
  { id: "wedding", label: "Wedding", icon: Gem },
  { id: "party", label: "Party", icon: PartyPopper },
  { id: "formal", label: "Formal", icon: Briefcase },
];

export default function OccasionSelector({ selected, onSelect }) {
  return (
    <div data-testid="occasion-selector" className="w-full">
      <p className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8] mb-4">
        What's the occasion?
      </p>
      <div className="flex flex-wrap gap-3">
        {OCCASIONS.map((occ) => {
          const isActive = selected === occ.id;
          const Icon = occ.icon;
          return (
            <button
              key={occ.id}
              data-testid={`occasion-${occ.id}`}
              onClick={() => onSelect(occ.id)}
              className={`
                flex items-center gap-2 px-5 py-2.5 rounded-full font-body text-sm font-medium
                transition-all duration-300 cursor-pointer
                ${
                  isActive
                    ? "bg-[#4F46E5]/20 border border-[#4F46E5] text-[#F8FAFC] shadow-[0_0_20px_rgba(79,70,229,0.2)]"
                    : "backdrop-blur-2xl bg-white/[0.03] border border-white/10 text-[#94A3B8] hover:bg-white/[0.06] hover:text-[#F8FAFC] hover:border-white/20"
                }
              `}
            >
              <Icon className={`w-4 h-4 ${isActive ? "text-[#4F46E5]" : ""}`} />
              {occ.label}
            </button>
          );
        })}
      </div>
    </div>
  );
}
