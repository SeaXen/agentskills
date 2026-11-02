import { getHomeMarkdown, markdownResponse } from "@/lib/llm-content";

export const revalidate = false;

export function GET() {
  return markdownResponse(getHomeMarkdown());
}
