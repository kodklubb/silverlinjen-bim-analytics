import type { LucideIcon } from "lucide-react";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

interface StatCardProps {
  title: string;
  value: string | number;
  unit?: string;
  description?: string;
  icon: LucideIcon;
}

export function StatCard({
  title,
  value,
  unit,
  description,
  icon: Icon,
}: StatCardProps) {
  return (
    <Card className="gap-0 shadow-sm">
      <CardContent className="space-y-4 p-5">
        <div className="flex items-center justify-between gap-3">
          <p className="text-sm font-medium text-muted-foreground">
            {title}
          </p>

          <div className="flex size-10 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
            <Icon className="size-5" />
          </div>
        </div>

        <div className="flex flex-wrap items-baseline gap-1.5">
          <span className="text-3xl font-semibold tracking-tight tabular-nums">
            {value}
          </span>

          {unit && (
            <span className="text-sm font-medium text-muted-foreground">
              {unit}
            </span>
          )}
        </div>

        {description && (
          <p className="text-xs leading-relaxed text-muted-foreground">
            {description}
          </p>
        )}
      </CardContent>
    </Card>
  );
}