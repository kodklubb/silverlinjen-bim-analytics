import type { z } from "zod";

import type {
  quantityKpisSchema,
  categoryBreakdownSchema,
  structuralElementSchema,
  quantityReportSchema,
} from "@/lib/schemas/quantities";

export type QuantityKPIs = z.infer<
  typeof quantityKpisSchema
>;

export type CategoryBreakdown = z.infer<
  typeof categoryBreakdownSchema
>;

export type StructuralElement = z.infer<
  typeof structuralElementSchema
>;

export type QuantityReport = z.infer<
  typeof quantityReportSchema
>;