import type { SVGProps } from "react";

export function BrandLogo(
  props: SVGProps<SVGSVGElement>
) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 48 48"
      fill="none"
      aria-hidden="true"
      {...props}
    >
      <g
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinejoin="round"
        strokeLinecap="round"
      >
        {/* Bridge deck */}
        <path d="M5 19L30 9L43 15L18 25Z" />

        {/* Structural thickness */}
        <path d="M5 19V24L18 30L43 20V15" />
        <path d="M18 25V30" />

        {/* Supporting columns */}
        <path d="M12 27V39L17 41V30" />
        <path d="M30 26V34L35 32V23" />

        {/* BIM model subdivisions */}
        <path d="M14 16L27 22M22 12L35 18" />

        {/* Digital reference axis */}
        <path
          d="M7 42L42 29"
          opacity=".5"
          strokeDasharray="2 3"
        />
      </g>
    </svg>
  );
}