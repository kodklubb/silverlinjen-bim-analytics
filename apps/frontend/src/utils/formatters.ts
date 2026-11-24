export function formatNumber(
  value: number | null | undefined,
  decimals = 0
): string {
  if (value == null || !Number.isFinite(value)) {
    return "—";
  }

  return new Intl.NumberFormat("en-US", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  }).format(value);
}

export function formatVolume(
  value: number | null | undefined,
  decimals = 2
): string {
  return formatNumber(value, decimals);
}

export function formatPercentage(
  value: number | null | undefined,
  decimals = 1
): string {
  if (value == null || !Number.isFinite(value)) {
    return "—";
  }

  return `${formatNumber(value, decimals)}%`;
}