import { VolumeBarChart } from "./volume-bar-chart";
import { VolumeDonutChart } from "./volume-donut-chart";
import { ElementCountChart } from "./element-count-chart";
import { VolumeParetoChart } from "./volume-pareto-chart";

import type { CategoryBreakdown } from "@/types/quantities";

interface QuantityChartsProps {
  categories: CategoryBreakdown[];
}

export function QuantityCharts({
  categories,
}: QuantityChartsProps) {
  return (
    <div className="space-y-4">

      {/* Volume analysis */}
      <div className="grid grid-cols-1 gap-4 xl:grid-cols-5">

        <div className="min-w-0 xl:col-span-3">
          <VolumeBarChart categories={categories} />
        </div>

        <div className="min-w-0 xl:col-span-2">
          <VolumeDonutChart categories={categories} />
        </div>

      </div>

      {/* Element and cumulative analysis */}
      <div className="grid grid-cols-1 gap-4 xl:grid-cols-2">

        <ElementCountChart categories={categories} />

        <VolumeParetoChart categories={categories} />

      </div>

    </div>
  );
}