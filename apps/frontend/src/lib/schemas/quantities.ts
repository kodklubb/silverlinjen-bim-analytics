import { z } from "zod";

export const quantityKpisSchema = z.object({
  total_elements: z.number().int().nonnegative(),
  structural_elements: z.number().int().nonnegative(),
  excluded_elements: z.number().int().nonnegative(),
  total_volume_m3: z.number().nullable(),
  category_count: z.number().int().nonnegative(),
  material_count: z.number().int().nonnegative(),
});

export const categoryBreakdownSchema = z.object({
  category: z.string(),
  element_count: z.number().int().nonnegative(),
  total_volume_m3: z.number().nullable(),
  average_volume_m3: z.number().nullable(),
  min_volume_m3: z.number().nullable(),
  max_volume_m3: z.number().nullable(),
  volume_share_pct: z.number().nullable(),
});

export const structuralElementSchema = z.object({
  global_id: z.string(),
  ifc_class: z.string(),
  name: z.string().nullable(),
  category: z.string().nullable(),
  material: z.string().nullable(),
  net_volume_m3: z.number().nullable(),
});

export const quantityReportSchema = z.object({
  project: z.string(),
  model: z.string(),
  section: z.string(),
  source: z.string(),

  kpis: quantityKpisSchema,

  categories: z.array(categoryBreakdownSchema),

  elements: z.array(structuralElementSchema),
});