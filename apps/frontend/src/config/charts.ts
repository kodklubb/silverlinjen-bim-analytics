export const CATEGORY_COLORS: Record<string, string> = {
  "Bridge Deck": "var(--chart-1)",
  Walls: "var(--chart-2)",
  Foundations: "var(--chart-3)",
  Columns: "var(--chart-4)",
  Beams: "var(--chart-5)",
};

export function getCategoryColor(
  category: string
): string {
  return CATEGORY_COLORS[category] ?? "var(--muted-foreground)";
}

export const CHART_THEME = {
  grid: "var(--border)",
  axis: "var(--muted-foreground)",
  text: "var(--foreground)",
  background: "var(--card)",
  cumulative: "var(--chart-2)",
  threshold: "var(--warning)",
} as const;