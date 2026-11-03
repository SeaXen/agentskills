import asyncio
import json
import os
import sys
from pathlib import Path
from playwright.async_api import async_playwright

LMS_BASE = "https://lms.synapsepg.org"
USERNAME = os.environ.get("SYNAPSE_USER", "01683048886")
PASSWORD = Path(__file__).parent.joinpath(".creds").read_text().strip()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(f"{LMS_BASE}/videos/6a243060585213c2b6777ef9/lecture", wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            await page.get_by_placeholder("Enter mobile number").fill(USERNAME)
            await page.get_by_placeholder("Type your password").fill(PASSWORD)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda url: "/login" not in url, timeout=30000)
        await page.goto(f"{LMS_BASE}/videos/6a243060585213c2b6777ef9/lecture", wait_until="domcontentloaded", timeout=30000)

        details = await page.evaluate("""
            () => {
                const cards = document.querySelectorAll('.student-video-card-wrap');
                return Array.from(cards).map(c => {
                    const allAttrs = {};
                    for (const a of c.attributes) allAttrs[a.name] = a.value;
                    let reactKey = null;
                    for (const key in c) {
                        if (key.startsWith('__reactProps')) {
                            const p = c[key];
                            if (p) {
                                if (p.onClick) reactKey = String(p.onClick).substring(0, 300);
                            }
                            break;
                        }
                    }
                    const inner = c.outerHTML;
                    const idMatch = inner.match(/[a-f0-9]{20,30}/g);
                    return {
                        allAttrs,
                        onclickStr: reactKey,
                        idsInHTML: idMatch,
                        text: c.innerText.substring(0, 100),
                    };
                });
            }
        """)
        print(json.dumps(details, indent=2, default=str))
        await browser.close()

asyncio.run(main())
