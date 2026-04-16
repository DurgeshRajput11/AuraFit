import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogDescription,
} from "../components/ui/dialog";
import { Shirt, Footprints, Watch, X } from "lucide-react";

const CATEGORY_ICONS = {
  top: Shirt,
  bottom: Shirt,
  shoes: Footprints,
  accessories: Watch,
};

const CATEGORY_LABELS = {
  top: "Top",
  bottom: "Bottom",
  shoes: "Footwear",
  accessories: "Accessory",
};

export default function OutfitDetail({ outfit, open, onClose }) {
  if (!outfit) return null;

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent
        data-testid="outfit-detail-modal"
        className="max-w-3xl w-[95vw] p-0 bg-[#0F0F16] border-white/5 rounded-3xl overflow-hidden max-h-[90vh] overflow-y-auto"
      >
        <DialogTitle className="sr-only">{outfit.title}</DialogTitle>
        <DialogDescription className="sr-only">{outfit.description}</DialogDescription>
        {/* Close button */}
        <button
          data-testid="outfit-detail-close"
          onClick={() => onClose(false)}
          className="absolute top-4 right-4 z-20 p-2 rounded-full bg-black/50 backdrop-blur-md border border-white/10 text-[#94A3B8] hover:text-white transition-colors"
        >
          <X className="w-4 h-4" />
        </button>

        {/* Hero Image */}
        <div className="relative w-full aspect-[16/10]">
          <img
            src={outfit.image_url}
            alt={outfit.title}
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-[#0F0F16] via-[#0F0F16]/30 to-transparent" />

          {/* Tags overlay */}
          <div className="absolute bottom-6 left-6 right-6">
            <div className="flex flex-wrap gap-2 mb-3">
              <span className="px-3 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-[#4F46E5]/30 text-[#4F46E5] border border-[#4F46E5]/30 backdrop-blur-md">
                {outfit.occasion}
              </span>
              <span className="px-3 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-white/10 text-[#94A3B8] border border-white/10 backdrop-blur-md">
                {outfit.gender}
              </span>
              <span className="px-3 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-white/10 text-[#94A3B8] border border-white/10 backdrop-blur-md">
                {outfit.season}
              </span>
              <span className="px-3 py-1 rounded-full text-[10px] uppercase tracking-wider font-body font-semibold bg-white/10 text-[#94A3B8] border border-white/10 backdrop-blur-md">
                {outfit.style}
              </span>
            </div>
            <h2 className="font-heading text-3xl md:text-4xl tracking-tight text-[#F8FAFC]">
              {outfit.title}
            </h2>
          </div>
        </div>

        {/* Body */}
        <div className="px-6 pb-8 -mt-1">
          <p className="font-body text-base text-[#94A3B8] leading-relaxed mb-8">
            {outfit.description}
          </p>

          {/* Clothing Items */}
          <div className="space-y-1">
            <p className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8] mb-4">
              What You Need
            </p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {outfit.items.map((item, i) => {
                const Icon = CATEGORY_ICONS[item.category] || Shirt;
                return (
                  <div
                    key={i}
                    data-testid={`outfit-item-${i}`}
                    className="flex items-start gap-3 p-4 rounded-2xl bg-white/[0.03] border border-white/5 hover:border-white/10 transition-colors"
                  >
                    <div className="flex-shrink-0 w-9 h-9 rounded-xl bg-[#4F46E5]/10 flex items-center justify-center">
                      <Icon className="w-4 h-4 text-[#4F46E5]" />
                    </div>
                    <div className="min-w-0">
                      <p className="font-body text-sm font-medium text-[#F8FAFC]">
                        {item.name}
                      </p>
                      <p className="font-body text-xs text-[#94A3B8] mt-0.5">
                        {CATEGORY_LABELS[item.category]} &middot; {item.color}
                      </p>
                      <p className="font-body text-xs text-[#94A3B8]/70 mt-1">
                        {item.description}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Tags */}
          {outfit.tags && outfit.tags.length > 0 && (
            <div className="mt-8">
              <p className="text-xs uppercase tracking-[0.2em] font-body font-semibold text-[#94A3B8] mb-3">
                Style Tags
              </p>
              <div className="flex flex-wrap gap-2">
                {outfit.tags.map((tag) => (
                  <span
                    key={tag}
                    className="px-3 py-1.5 rounded-full text-xs font-body text-[#94A3B8] bg-white/[0.04] border border-white/5"
                  >
                    #{tag}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
