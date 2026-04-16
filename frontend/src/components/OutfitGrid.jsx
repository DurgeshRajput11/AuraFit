import OutfitCard from "./OutfitCard";

export default function OutfitGrid({ outfits, onSelect }) {
  return (
    <div
      data-testid="outfit-grid"
      className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 stagger-children"
    >
      {outfits.map((outfit, i) => (
        <OutfitCard
          key={outfit.id}
          outfit={outfit}
          index={i}
          onSelect={onSelect}
        />
      ))}
    </div>
  );
}
