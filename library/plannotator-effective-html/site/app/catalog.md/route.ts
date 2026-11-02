import { getCatalogMarkdown, markdownResponse } from "@/lib/llm-content";

export const revalidate = false;

export function GET() {
  return markdownResponse(getCatalogMarkdown());
}
