import type { Metadata } from "next";
import { Ruler } from "lucide-react";

import { Badge } from "@/components/ui/badge";

import { QuantityReport } from
  "@/components/reports/quantities/quantity-report";

export const metadata: Metadata = {
  title: "Quantity Take-Off",
};

export default function QuantitiesPage() {
  return (
    <div className="space-y-6">

      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="space-y-2">

          <div className="flex items-center gap-2">
            <Ruler className="size-6 text-primary" />

            <h1 className="text-2xl font-semibold tracking-tight md:text-3xl">
              Quantity Take-Off
            </h1>
          </div>

          <p className="text-sm text-muted-foreground">
            Structural quantities and engineering insights
            for infrastructure models.
          </p>

        </div>

        <Badge variant="secondary">
          Viadukten — Del 1
        </Badge>
      </div>

      <QuantityReport />

    </div>
  );
}