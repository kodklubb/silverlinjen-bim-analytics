import type { Metadata } from "next";
import { Inter, Geist_Mono } from "next/font/google";
import { AppProviders } from "@/components/providers/app-providers";

import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Silverlinjen BIM Analytics",
    template: "%s | Silverlinjen BIM Analytics",
  },
  description:
    "OpenBIM infrastructure analytics platform for quantity take-off, cost estimation, carbon analysis, and model validation.",
  applicationName: "Silverlinjen BIM Analytics",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${inter.variable} ${geistMono.variable}`}
    >
      <body className={`${inter.className} antialiased`}>
        <AppProviders>
          {children}
        </AppProviders>
      </body>
    </html>
  );
}