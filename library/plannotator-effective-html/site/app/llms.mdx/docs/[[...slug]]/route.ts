import { getGuideMarkdown, markdownResponse } from "@/lib/llm-content";
import { source } from "@/lib/source";
import { notFound } from "next/navigation";

interface RouteProps {
  params: Promise<{ slug?: string[] }>;
}

/** Pre-render each guide's Markdown representation at build time. */
export const revalidate = false;

/** Serve the processed Markdown for a guide page. */
export async function GET(_request: Request, { params }: RouteProps) {
  const { slug } = await params;
  const page = source.getPage(slug);

  if (!page) notFound();

  return markdownResponse(await getGuideMarkdown(page));
}

/** Return every guide slug for static generation. */
export function generateStaticParams() {
  return source.generateParams();
}
