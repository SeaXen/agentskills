import type { BaseLayoutProps } from "fumadocs-ui/layouts/shared";

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: (
        <span className="docs-wordmark">
          <span className="docs-wordmark-mark" aria-hidden="true" />
          Effective HTML
        </span>
      ),
      url: "/",
    },
    links: [
      {
        text: (
          <span className="docs-catalog-link">
            <span className="docs-catalog-star" aria-hidden="true">
              ★
            </span>
            Catalog
          </span>
        ),
        url: "/catalog",
      },
      {
        text: "GitHub",
        url: "https://github.com/plannotator/effective-html",
        external: true,
      },
    ],
    githubUrl: "https://github.com/plannotator/effective-html",
  };
}
