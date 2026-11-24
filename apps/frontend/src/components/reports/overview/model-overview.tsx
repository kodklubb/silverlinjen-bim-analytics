"use client";

import { AlertCircle, RefreshCw } from "lucide-react";

import { useQuantityReport } from "@/hooks/use-quantity-report";

import { QuantityKPIs } from
  "@/components/reports/quantities/quantity-kpis";

import { StructuralElementsTable } from
  "./structural-elements-table";

import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

export function ModelOverview() {
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
      <div className="space-y-6" aria-busy="true">
        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          {Array.from({ length: 4 }).map((_, index) => (
            <Skeleton
              key={index}
              className="h-44 rounded-xl"
            />
          ))}
        </div>

        <Skeleton className="h-96 rounded-xl" />
      </div>
    );
  }

  if (isError && !data) {
    return (
      <Card>
        <CardContent className="flex min-h-56 flex-col items-center justify-center gap-4 p-6">
          <AlertCircle className="size-8 text-destructive" />

          <p className="text-sm font-medium">
            Unable to load model data
          </p>

          <p className="text-sm text-muted-foreground">
            {error.message}
          </p>

          <Button
            variant="outline"
            disabled={isFetching}
            onClick={() => void refetch()}
          >
            Try again
          </Button>
        </CardContent>
      </Card>
    );
  }

  if (!data) return null;

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

      <StructuralElementsTable elements={data.elements} />
    </div>
  );
}