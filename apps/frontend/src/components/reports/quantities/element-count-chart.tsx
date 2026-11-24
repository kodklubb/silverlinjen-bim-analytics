"use client";

import {
  BarChart,
  Bar,
  Cell,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  LabelList,
  ResponsiveContainer,
} from "recharts";

import { ChartCard } from "@/components/charts/chart-card";

import {
  getCategoryColor,
  CHART_THEME,
} from "@/config/charts";

import { formatNumber } from "@/utils/formatters";

import type { CategoryBreakdown } from "@/types/quantities";

export function ElementCountChart({
  categories,
}: {
  categories: CategoryBreakdown[];
}) {
  const chartData = [...categories].sort(
    (a, b) => b.element_count - a.element_count
  );

  return (
    <ChartCard
      title="Element Count by Category"
      description="Number of structural elements in the IFC model"
    >
      <div className="h-[320px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            margin={{
              top: 25,
              right: 10,
              bottom: 10,
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
              allowDecimals={false}
              tickLine={false}
              axisLine={false}
              width={35}
              tick={{
                fill: CHART_THEME.axis,
                fontSize: 11,
              }}
            />

            <Tooltip
              cursor={{ fill: "var(--muted)" }}
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
              formatter={(value) => [
                formatNumber(Number(value)),
                "Elements",
              ]}
            />

            <Bar
              dataKey="element_count"
              radius={[5, 5, 0, 0]}
              maxBarSize={60}
              animationDuration={650}
            >
              {chartData.map((item) => (
                <Cell
                  key={item.category}
                  fill={getCategoryColor(item.category)}
                />
              ))}

              <LabelList
                dataKey="element_count"
                position="top"
                fill={CHART_THEME.text}
                fontSize={12}
              />
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </ChartCard>
  );
}