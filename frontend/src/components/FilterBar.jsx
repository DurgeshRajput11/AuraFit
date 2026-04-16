import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../components/ui/select";

const GENDERS = [
  { value: "men", label: "Men" },
  { value: "women", label: "Women" },
];

const SEASONS = [
  { value: "all", label: "All Seasons" },
  { value: "summer", label: "Summer" },
  { value: "winter", label: "Winter" },
  { value: "spring", label: "Spring" },
  { value: "fall", label: "Fall" },
];

const STYLES = [
  { value: "", label: "All Styles" },
  { value: "casual", label: "Casual" },
  { value: "formal", label: "Formal" },
  { value: "streetwear", label: "Streetwear" },
  { value: "elegant", label: "Elegant" },
  { value: "minimalist", label: "Minimalist" },
  { value: "bohemian", label: "Bohemian" },
];

export default function FilterBar({ gender, season, style, onGenderChange, onSeasonChange, onStyleChange }) {
  return (
    <div data-testid="filter-bar" className="flex flex-wrap items-end gap-4">
      <div className="flex flex-col gap-1.5">
        <label className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8]">
          Gender
        </label>
        <Select value={gender} onValueChange={onGenderChange}>
          <SelectTrigger
            data-testid="filter-gender"
            className="w-[140px] bg-[#0F0F16] border-white/10 text-[#F8FAFC] font-body text-sm rounded-xl focus:ring-[#4F46E5] focus:border-[#4F46E5]"
          >
            <SelectValue placeholder="Gender" />
          </SelectTrigger>
          <SelectContent className="bg-[#0F0F16] border-white/10">
            {GENDERS.map((g) => (
              <SelectItem
                key={g.value}
                value={g.value}
                className="text-[#F8FAFC] font-body text-sm focus:bg-[#4F46E5]/20 focus:text-[#F8FAFC]"
              >
                {g.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className="flex flex-col gap-1.5">
        <label className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8]">
          Season
        </label>
        <Select value={season} onValueChange={onSeasonChange}>
          <SelectTrigger
            data-testid="filter-season"
            className="w-[160px] bg-[#0F0F16] border-white/10 text-[#F8FAFC] font-body text-sm rounded-xl focus:ring-[#4F46E5] focus:border-[#4F46E5]"
          >
            <SelectValue placeholder="Season" />
          </SelectTrigger>
          <SelectContent className="bg-[#0F0F16] border-white/10">
            {SEASONS.map((s) => (
              <SelectItem
                key={s.value}
                value={s.value}
                className="text-[#F8FAFC] font-body text-sm focus:bg-[#4F46E5]/20 focus:text-[#F8FAFC]"
              >
                {s.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className="flex flex-col gap-1.5">
        <label className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8]">
          Style
        </label>
        <Select value={style} onValueChange={onStyleChange}>
          <SelectTrigger
            data-testid="filter-style"
            className="w-[160px] bg-[#0F0F16] border-white/10 text-[#F8FAFC] font-body text-sm rounded-xl focus:ring-[#4F46E5] focus:border-[#4F46E5]"
          >
            <SelectValue placeholder="All Styles" />
          </SelectTrigger>
          <SelectContent className="bg-[#0F0F16] border-white/10">
            {STYLES.map((s) => (
              <SelectItem
                key={s.value || "all-styles"}
                value={s.value || "all"}
                className="text-[#F8FAFC] font-body text-sm focus:bg-[#4F46E5]/20 focus:text-[#F8FAFC]"
              >
                {s.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}
