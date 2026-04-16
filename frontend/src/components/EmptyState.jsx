export default function EmptyState() {
  return (
    <div data-testid="empty-state" className="flex flex-col items-center justify-center py-16 animate-fade-in">
      <div className="w-24 h-24 rounded-full bg-[#1E1E2F] flex items-center justify-center mb-6">
        <span className="text-3xl">👕</span>
      </div>

      <h3 className="font-heading text-xl md:text-2xl tracking-tight text-[#F8FAFC] mb-2">
        No Looks Found
      </h3>

      <p className="font-body text-sm text-[#94A3B8] text-center max-w-sm">
        Try adjusting your filters or selecting a different occasion to discover your perfect outfit.
      </p>
    </div>
  );
}