import { useState } from "react";
import { Eye } from "lucide-react";

export default function OutfitCard({ outfit, index, onSelect }) {
  const [imageLoaded, setImageLoaded] = useState(false);

  return (
    <div
      data-testid={`outfit-card-${index}`}
      onClick={() => onSelect(outfit)}
      className="group relative aspect-[3/4] rounded-3xl overflow-hidden cursor-pointer transition-all duration-500 hover:scale-[1.02] hover:shadow-[0_20px_60px_rgba(0,0,0,0.5)]"
      style={{ animationDelay: `${index * 0.1}s` }}
    >
      {/* Shimmer placeholder */}
      {!imageLoaded && (
        <div className="absolute inset-0 img-shimmer rounded-3xl" />
      )}

      {/* Image */}
      <img
        src={outfit.image_url}
        alt={outfit.title}
        loading="lazy"
        onLoad={() => setImageLoaded(true)}
        className={`absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 ${
          imageLoaded ? "opacity-100" : "opacity-0"
        }`}
      />

      {/* Overlay gradient */}
      <div className="absolute inset-0 card-overlay opacity-80 group-hover:opacity-90 transition-opacity duration-300" />

      {/* Content */}
      <div className="absolute bottom-0 left-0 right-0 p-5 md:p-6">
        {/* Tags */}
        <div className="flex flex-wrap gap-1.5 mb-3 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-2 group-hover:translate-y-0">
          <span className="px-2.5 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-[#4F46E5]/30 text-[#4F46E5] border border-[#4F46E5]/20">
            {outfit.occasion}
          </span>
          <span className="px-2.5 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-white/10 text-[#94A3B8] border border-white/10">
            {outfit.style}
          </span>
        </div>

        <h3 className="font-heading text-xl md:text-2xl tracking-tight text-[#F8FAFC] mb-1.5">
          {outfit.title}
        </h3>
        <p className="font-body text-sm text-[#94A3B8] line-clamp-2 mb-4">
          {outfit.description}
        </p>

        {/* View button on hover */}
        <div className="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-2 group-hover:translate-y-0">
          <span className="inline-flex items-center gap-1.5 text-xs font-body font-semibold text-[#4F46E5] tracking-wide uppercase">
            <Eye className="w-3.5 h-3.5" />
            View Details
          </span>
        </div>
      </div>
    </div>
  );
}
