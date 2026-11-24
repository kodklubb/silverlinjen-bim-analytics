"use client";

import {
  BarChart,
  Bar,
  Cell,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { ChartCard } from "@/components/charts/chart-card";

import {
  getCategoryColor,
  CHART_THEME,
} from "@/config/charts";

import { formatVolume } from "@/utils/formatters";

import type { CategoryBreakdown } from "@/types/quantities";

interface VolumeBarChartProps {
  categories: CategoryBreakdown[];
}

export function VolumeBarChart({
  categories,
}: VolumeBarChartProps) {
  const chartData = categories
    .filter((item) => item.total_volume_m3 !== null)
    .sort(
      (a, b) =>
        (b.total_volume_m3 ?? 0) -
        (a.total_volume_m3 ?? 0)
    );

  return (
    <ChartCard
      title="Volume by Category"
      description="Net structural volume by engineering category (m³)"
    >
      <div className="h-[390px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            layout="vertical"
            margin={{
              top: 10,
              right: 24,
              bottom: 10,
              left: 5,
            }}
          >
            <CartesianGrid
              horizontal={false}
              stroke={CHART_THEME.grid}
              strokeDasharray="3 3"
            />

            <XAxis
              type="number"
              tickLine={false}
              axisLine={false}
              tick={{
                fill: CHART_THEME.axis,
                fontSize: 11,
              }}
              tickFormatter={(value) =>
                formatVolume(Number(value), 0)
              }
            />

            <YAxis
              type="category"
              dataKey="category"
              width={100}
              tickLine={false}
              axisLine={false}
              tick={{
                fill: CHART_THEME.axis,
                fontSize: 12,
              }}
            />

            <Tooltip
              cursor={{
                fill: "var(--muted)",
              }}
              contentStyle={{
                backgroundColor: "var(--card)",
                borderColor: "var(--border)",
                borderRadius: 10,
                fontSize: 12,
                color: "var(--foreground)",
              }}
              labelStyle={{
                color: "var(--foreground)",
              }}
              itemStyle={{
                color: "var(--foreground)",
              }}
              formatter={(value) => [
                `${formatVolume(Number(value))} m³`,
                "Net volume",
              ]}
            />

            <Bar
              dataKey="total_volume_m3"
              radius={[0, 5, 5, 0]}
              barSize={30}
              animationDuration={650}
            >
              {chartData.map((item) => (
                <Cell
                  key={item.category}
                  fill={getCategoryColor(item.category)}
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </ChartCard>
  );
}