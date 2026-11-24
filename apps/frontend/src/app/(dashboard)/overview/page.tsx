import type { Metadata } from "next";
import { LayoutDashboard } from "lucide-react";

import { Badge } from "@/components/ui/badge";

import { ModelOverview } from
  "@/components/reports/overview/model-overview";

export const metadata: Metadata = {
  title: "Infrastructure Overview",
};

export default function OverviewPage() {
  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <LayoutDashboard className="size-6 text-primary" />

            <h1 className="text-2xl font-semibold tracking-tight md:text-3xl">
              Infrastructure Overview
            </h1>
          </div>

          <p className="text-sm text-muted-foreground">
            Structural model information and extracted
            IFC element data.
          </p>
        </div>

        <Badge variant="secondary">
          Viadukten — Del 1
        </Badge>
      </div>

      <ModelOverview />
    </div>
  );
}