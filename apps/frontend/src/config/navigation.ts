import {
  LayoutDashboard,
  Ruler,
  Layers,
  Calculator,
  Leaf,
  ShieldCheck,
  GitCompareArrows,
  Box,
  SlidersHorizontal,
  FileDown,
  type LucideIcon,
} from "lucide-react";

export interface NavigationItem {
  title: string;
  href: string;
  icon: LucideIcon;
  enabled: boolean;
}

export const navigationItems: NavigationItem[] = [
  {
    title: "Overview",
    href: "/overview",
    icon: LayoutDashboard,
    enabled: true,
  },
  {
    title: "Quantity Take-Off",
    href: "/quantities",
    icon: Ruler,
    enabled: true,
  },
  {
    title: "Material Analytics",
    href: "/materials",
    icon: Layers,
    enabled: false,
  },
  {
    title: "Cost Estimation",
    href: "/costs",
    icon: Calculator,
    enabled: false,
  },
  {
    title: "Carbon Analysis",
    href: "/carbon",
    icon: Leaf,
    enabled: false,
  },
  {
    title: "Data Quality",
    href: "/quality",
    icon: ShieldCheck,
    enabled: false,
  },
  {
    title: "IFC vs. Revit",
    href: "/comparison",
    icon: GitCompareArrows,
    enabled: false,
  },
  {
    title: "3D Model Viewer",
    href: "/model-viewer",
    icon: Box,
    enabled: false,
  },
  {
    title: "Scenario Analysis",
    href: "/scenarios",
    icon: SlidersHorizontal,
    enabled: false,
  },
  {
    title: "Reports & Export",
    href: "/reports",
    icon: FileDown,
    enabled: false,
  },
];