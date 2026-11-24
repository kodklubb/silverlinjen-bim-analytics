"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { BrandLogo } from "@/components/brand/brand-logo";

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
  SidebarSeparator,
  useSidebar,
} from "@/components/ui/sidebar";

import { navigationItems } from "@/config/navigation";

export function AppSidebar() {
  const pathname = usePathname();
  const { setOpenMobile } = useSidebar();

  return (
    <Sidebar collapsible="icon">
      <SidebarHeader className="p-3">
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton
              size="lg"
              tooltip="Silverlinjen BIM Analytics"
              render={<Link href="/quantities" />}
            >
              <div className="flex size-9 shrink-0 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <BrandLogo className="size-8" />
              </div>

              <div className="grid flex-1 text-left leading-tight">
                <span className="truncate font-semibold tracking-wide text-white">
                  SILVERLINJEN
                </span>

                <span className="truncate text-xs text-sidebar-foreground">
                  BIM Analytics
                </span>
              </div>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>

      <SidebarSeparator />

      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel className="text-xs uppercase tracking-wider">
            Workspace
          </SidebarGroupLabel>

          <SidebarGroupContent>
            <SidebarMenu className="gap-1">
              {navigationItems.map((item) => {
                const isActive =
                  pathname === item.href ||
                  pathname.startsWith(`${item.href}/`);

                return (
                  <SidebarMenuItem key={item.href}>
                    {item.enabled ? (
                      <SidebarMenuButton
                        tooltip={item.title}
                        isActive={isActive}
                        aria-current={
                          isActive ? "page" : undefined
                        }
                        className="h-10 data-active:bg-sidebar-primary! data-active:text-sidebar-primary-foreground!"
                        render={
                          <Link
                            href={item.href}
                            onClick={() => setOpenMobile(false)}
                          />
                        }
                      >
                        <item.icon />
                        <span>{item.title}</span>
                      </SidebarMenuButton>
                    ) : (
                      <SidebarMenuButton
                        disabled
                        title="Coming soon"
                        aria-label={`${item.title} — Coming soon`}
                        className="h-10 opacity-45"
                      >
                        <item.icon />
                        <span>{item.title}</span>
                      </SidebarMenuButton>
                    )}
                  </SidebarMenuItem>
                );
              })}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>

      <SidebarSeparator />

      <SidebarFooter className="p-4">
        <div className="space-y-1 group-data-[collapsible=icon]:hidden">
          <p className="text-xs font-medium text-sidebar-foreground">
            OpenBIM Analytics Platform
          </p>

          <p className="text-[11px] text-sidebar-foreground/60">
            Version 0.1.0 · Development
          </p>
        </div>
      </SidebarFooter>

      <SidebarRail />
    </Sidebar>
  );
}