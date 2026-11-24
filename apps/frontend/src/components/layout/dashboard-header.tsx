"use client";

import { ChevronRight } from "lucide-react";

import { SidebarTrigger } from "@/components/ui/sidebar";
import { Separator } from "@/components/ui/separator";
import { Badge } from "@/components/ui/badge";

import { ThemeSwitcher } from "./theme-switcher";

export function DashboardHeader() {
  return (
    <header className="sticky top-0 z-20 flex h-16 shrink-0 items-center justify-between gap-3 border-b bg-background/95 px-4 backdrop-blur md:px-6">
      <div className="flex min-w-0 items-center gap-3">
        <SidebarTrigger />

        <Separator
          orientation="vertical"
          className="h-6"
        />

        <nav
          aria-label="Project breadcrumb"
          className="flex min-w-0 items-center gap-2 text-sm"
        >
          <span className="hidden text-muted-foreground lg:inline">
            Silverlinjen
          </span>

          <ChevronRight className="hidden size-4 shrink-0 text-muted-foreground lg:block" />

          <span className="truncate text-muted-foreground">
            Viadukten
          </span>

          <ChevronRight className="size-4 shrink-0 text-muted-foreground" />

          <span className="shrink-0 font-medium text-foreground">
            Del 1
          </span>
        </nav>
      </div>

      <div className="flex shrink-0 items-center gap-3">
        <Badge
          variant="outline"
          className="hidden md:inline-flex"
        >
          IFC Model
        </Badge>

        <ThemeSwitcher />
      </div>
    </header>
  );
}