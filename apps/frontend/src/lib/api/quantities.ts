import { apiGet } from "./client";

import { quantityReportSchema } from
  "@/lib/schemas/quantities";

import type { QuantityReport } from
  "@/types/quantities";

export async function getQuantityReport(
  signal?: AbortSignal
): Promise<QuantityReport> {
  const data = await apiGet(
    "/quantities/summary",
    signal
  );

  return quantityReportSchema.parse(data);
}