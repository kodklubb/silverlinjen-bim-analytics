"use client";

import {
  AlertCircle,
  RefreshCw,
} from "lucide-react";

import { useQuantityReport } from
  "@/hooks/use-quantity-report";

import { QuantityKPIs } from "./quantity-kpis";

import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { QuantityCharts } from "./quantity-charts";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

export function QuantityReport() {
  const {
    data,
    isPending,
    isError,
    error,
    isFetching,
    refetch,
  } = useQuantityReport();

  if (isPending) {
    return (
      <div
        aria-busy="true"
        aria-label="Loading quantity report"
        className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4"
      >
        {Array.from({ length: 4 }).map((_, index) => (
          <Card key={index}>
            <CardContent className="space-y-4 p-5">
              <Skeleton className="h-4 w-32" />
              <Skeleton className="h-9 w-40" />
              <Skeleton className="h-3 w-full" />
            </CardContent>
          </Card>
        ))}
      </div>
    );
  }

  if (isError && !data) {
    return (
      <Card className="border-destructive/30">
        <CardContent className="flex min-h-56 flex-col items-center justify-center gap-4 p-6 text-center">

          <AlertCircle className="size-9 text-destructive" />

          <h2 className="text-lg font-semibold">
            Unable to load quantity report
          </h2>

          <p className="max-w-md text-sm text-muted-foreground">
            {error.message}
          </p>

          <Button
            variant="outline"
            disabled={isFetching}
            onClick={() => void refetch()}
          >
            <RefreshCw
              className={`size-4 ${
                isFetching ? "animate-spin" : ""
              }`}
            />
            Try again
          </Button>

        </CardContent>
      </Card>
    );
  }

  if (!data) {
    return null;
  }

  return (
    <div className="space-y-6">

      <div className="flex flex-wrap items-center justify-between gap-3">

        <div className="flex items-center gap-2 text-xs text-muted-foreground">
          <span
            className={`size-2 rounded-full ${
              isError ? "bg-warning" : "bg-success"
            }`}
          />

          {isError
            ? "Refresh failed — showing cached data"
            : isFetching
              ? "Refreshing data..."
              : "API data loaded"}

          <span>·</span>
          <span>Source: {data.source}</span>
        </div>

        <Button
          variant="outline"
          size="sm"
          disabled={isFetching}
          onClick={() => void refetch()}
        >
          <RefreshCw
            className={`size-4 ${
              isFetching ? "animate-spin" : ""
            }`}
          />
          Refresh data
        </Button>

      </div>

      <QuantityKPIs kpis={data.kpis} />
<QuantityCharts categories={data.categories} />

    </div>
  );
}