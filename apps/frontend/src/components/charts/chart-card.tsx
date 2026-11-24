import type { ReactNode } from "react";

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";

interface ChartCardProps {
  title: string;
  description?: string;
  children: ReactNode;
  className?: string;
}

export function ChartCard({
  title,
  description,
  children,
  className,
}: ChartCardProps) {
  return (
    <Card
        className={`h-full min-w-0 shadow-sm ${className ?? ""}`}
    >
      <CardHeader>
        <CardTitle className="text-base font-semibold">
          {title}
        </CardTitle>

        {description && (
          <CardDescription>
            {description}
          </CardDescription>
        )}
      </CardHeader>

      <CardContent className="min-w-0">
        {children}
      </CardContent>
    </Card>
  );
}