"use client";

import { useQuery } from "@tanstack/react-query";

import { getQuantityReport } from
  "@/lib/api/quantities";

export const quantityReportQueryKey = [
  "quantities",
  "summary",
] as const;

export function useQuantityReport() {
  return useQuery({
    queryKey: quantityReportQueryKey,
    queryFn: ({ signal }) =>
      getQuantityReport(signal),
  });
}