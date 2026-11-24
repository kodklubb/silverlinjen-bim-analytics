"use client";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { ChartCard } from "@/components/charts/chart-card";

import { getCategoryColor } from "@/config/charts";

import {
  formatVolume,
  formatPercentage,
} from "@/utils/formatters";

import type { CategoryBreakdown } from "@/types/quantities";

interface VolumeDonutChartProps {
  categories: CategoryBreakdown[];
}

export function VolumeDonutChart({
  categories,
}: VolumeDonutChartProps) {
  const chartData = categories
    .filter(
      (item) =>
        item.total_volume_m3 !== null &&
        item.total_volume_m3 > 0
    )
    .map((item) => ({
      name: item.category,
      value: item.total_volume_m3 ?? 0,
      percentage: item.volume_share_pct,
      color: getCategoryColor(item.category),
    }))
    .sort((a, b) => b.value - a.value);

  const totalVolume = chartData.reduce(
    (sum, item) => sum + item.value,
    0
  );

  return (
    <ChartCard
      title="Volume Distribution"
      description="Share of total structural volume"
    >
      {chartData.length === 0 ? (
        <div className="flex min-h-64 items-center justify-center text-sm text-muted-foreground">
          No positive volume data available.
        </div>
      ) : (
        <div className="space-y-4">
          <div className="relative h-[230px] w-full">
            <ResponsiveContainer
              width="100%"
              height="100%"
            >
              <PieChart>
                <Pie
                  data={chartData}
                  dataKey="value"
                  nameKey="name"
                  cx="50%"
                  cy="50%"
                  innerRadius="65%"
                  outerRadius="90%"
                  paddingAngle={2}
                  cornerRadius={4}
                  stroke="var(--card)"
                  strokeWidth={2}
                  animationDuration={700}
                >
                  {chartData.map((item) => (
                    <Cell
                      key={item.name}
                      fill={item.color}
                    />
                  ))}
                </Pie>

                <Tooltip
                  contentStyle={{
                    backgroundColor: "var(--card)",
                    borderColor: "var(--border)",
                    borderRadius: 10,
                    fontSize: 12,
                    color: "var(--foreground)",
                  }}
                  itemStyle={{
                    color: "var(--foreground)",
                  }}
                  formatter={(value, name) => [
                    `${formatVolume(Number(value))} m³`,
                    name,
                  ]}
                />
              </PieChart>
            </ResponsiveContainer>

            <div className="pointer-events-none absolute inset-0 flex flex-col items-center justify-center">
              <span className="text-2xl font-semibold tracking-tight tabular-nums">
                {formatVolume(totalVolume)}
              </span>

              <span className="mt-1 text-xs text-muted-foreground">
                Total volume (m³)
              </span>
            </div>
          </div>

          <div className="space-y-3">
            {chartData.map((item) => (
              <div
                key={item.name}
                className="flex items-center justify-between gap-3"
              >
                <div className="flex min-w-0 items-center gap-2.5">
                  <span
                    className="size-2.5 shrink-0 rounded-full"
                    style={{
                      backgroundColor: item.color,
                    }}
                  />

                  <span className="truncate text-sm text-muted-foreground">
                    {item.name}
                  </span>
                </div>

                <span className="text-sm font-medium tabular-nums">
                  {formatPercentage(item.percentage)}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </ChartCard>
  );
}