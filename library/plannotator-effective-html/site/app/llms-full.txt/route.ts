import { getLlmsFull } from "@/lib/llm-content";

export const revalidate = false;

export async function GET() {
  return new Response((await getLlmsFull()).trimEnd() + "\n", {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
    },
  });
}
