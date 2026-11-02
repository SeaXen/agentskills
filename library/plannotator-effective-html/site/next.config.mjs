import { createMDX } from "fumadocs-mdx/next";

/** @type {import("next").NextConfig} */
const config = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/index.html.md",
        destination: "/index.md",
      },
      {
        source: "/catalog/index.html.md",
        destination: "/catalog.md",
      },
      {
        source: "/catalog/folio.md",
        destination: "/catalog.md",
      },
      {
        source: "/examples/index.html.md",
        destination: "/examples.md",
      },
      {
        source: "/docs/index.html.md",
        destination: "/docs.md",
      },
      {
        source: "/docs.md",
        destination: "/llms.mdx/docs",
      },
      {
        source: "/docs/:path*.md",
        destination: "/llms.mdx/docs/:path*",
      },
    ];
  },
};

const withMDX = createMDX();

export default withMDX(config);
