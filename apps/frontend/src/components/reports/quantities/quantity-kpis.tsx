import {
  Box,
  Layers,
  LayoutGrid,
  Database,
} from "lucide-react";

import { StatCard } from "@/components/common/stat-card";

import type { QuantityKPIs as QuantityKPIsData } from
  "@/types/quantities";

import {
  formatNumber,
  formatVolume,
} from "@/utils/formatters";

interface QuantityKPIsProps {
  kpis: QuantityKPIsData;
}

export function QuantityKPIs({
  kpis,
}: QuantityKPIsProps) {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="Total Structural Volume"
        value={formatVolume(kpis.total_volume_m3)}
        unit="m³"
        description="Net volume of structural elements"
        icon={Box}
      />

      <StatCard
        title="Structural Elements"
        value={formatNumber(kpis.structural_elements)}
        description={`Of ${formatNumber(kpis.total_elements)} IFC elements`}
        icon={Layers}
      />

      <StatCard
        title="Structural Categories"
        value={formatNumber(kpis.category_count)}
        description="Classified structural categories"
        icon={LayoutGrid}
      />

      <StatCard
        title="Material Types"
        value={formatNumber(kpis.material_count)}
        description="Unique structural materials"
        icon={Database}
      />

    </div>
  );
}