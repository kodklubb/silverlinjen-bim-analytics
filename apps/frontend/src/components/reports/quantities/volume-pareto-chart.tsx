"use client";

import {
  ComposedChart,
  Bar,
  Cell,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ReferenceLine,
  ResponsiveContainer,
} from "recharts";

import { ChartCard } from "@/components/charts/chart-card";

import {
  getCategoryColor,
  CHART_THEME,
} from "@/config/charts";

import { formatPercentage } from "@/utils/formatters";

import type { CategoryBreakdown } from "@/types/quantities";

export function VolumeParetoChart({
  categories,
}: {
  categories: CategoryBreakdown[];
}) {
  const sortedCategories = categories
    .filter(
      (item) =>
        item.volume_share_pct !== null &&
        item.volume_share_pct > 0
    )
    .sort(
      (a, b) =>
        (b.volume_share_pct ?? 0) -
        (a.volume_share_pct ?? 0)
    );

  const chartData = sortedCategories.map(
    (item, index) => ({
      category: item.category,

      volumeShare: item.volume_share_pct ?? 0,

      cumulativeShare: sortedCategories
        .slice(0, index + 1)
        .reduce(
          (sum, category) =>
            sum + (category.volume_share_pct ?? 0),
          0
        ),
    })
  );

  return (
    <ChartCard
      title="Volume Pareto Analysis"
      description="Individual and cumulative contribution to total volume"
    >
      <div className="h-[320px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart
            data={chartData}
            margin={{
              top: 20,
              right: 15,
              bottom: 5,
              left: 0,
            }}
          >
            <CartesianGrid
              vertical={false}
              stroke={CHART_THEME.grid}
              strokeDasharray="3 3"
            />

            <XAxis
              dataKey="category"
              tickLine={false}
              axisLine={false}
              interval={0}
              tick={{
                fill: CHART_THEME.axis,
                fontSize: 11,
              }}
            />

            <YAxis
              domain={[0, 100]}
              ticks={[0, 25, 50, 75, 100]}
              tickLine={false}
              axisLine={false}
              width={45}
              tick={{
                fill: CHART_THEME.axis,
                fontSize: 11,
              }}
              tickFormatter={(value) => `${value}%`}
            />

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
                formatPercentage(Number(value), 2),
                name,
              ]}
            />

            <Legend
              iconSize={10}
              wrapperStyle={{ fontSize: 12 }}
            />

            <ReferenceLine
              y={80}
              stroke={CHART_THEME.threshold}
              strokeDasharray="5 5"
              label={{
                value: "80%",
                position: "insideTopRight",
                fill: CHART_THEME.threshold,
                fontSize: 11,
              }}
            />

            <Bar
              dataKey="volumeShare"
              name="Volume share"
              fill="var(--chart-1)"
              maxBarSize={45}
              radius={[4, 4, 0, 0]}
              animationDuration={650}
            >
              {chartData.map((item) => (
                <Cell
                  key={item.category}
                  fill={getCategoryColor(item.category)}
                />
              ))}
            </Bar>

            <Line
              type="linear"
              dataKey="cumulativeShare"
              name="Cumulative share"
              stroke={CHART_THEME.cumulative}
              strokeWidth={2.5}
              dot={{
                r: 4,
                fill: CHART_THEME.cumulative,
              }}
              activeDot={{ r: 6 }}
              animationDuration={700}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </div>
    </ChartCard>
  );
}