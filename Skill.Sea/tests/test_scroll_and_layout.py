import os
import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        page.goto('http://127.0.0.1:8080', wait_until='networkidle')

        print("Testing Desktop Mouse Wheel Scroll...")
        # 1. Skill Hub Scroll
        page.mouse.move(640, 400)
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
        sy1 = page.evaluate('window.scrollY')
        print(f"Skill-Hub scrollY after wheel 600: {sy1} (Expect > 0)")
        assert sy1 > 0, f"Expected window.scrollY > 0, got {sy1}"

        # 2. Hot-Set View Scroll & Overlap Verification
        page.locator('#tab-hotset').click()
        page.wait_for_timeout(300)
        h_info = page.evaluate('''() => {
            return {
                scrollY: window.scrollY,
                scrollHeight: document.body.scrollHeight,
                windowHeight: window.innerHeight,
                elementUnderMouse: document.elementFromPoint(640, 400)?.tagName
            }
        }''')
        print("Hotset scroll info before wheel:", h_info)
        page.mouse.move(640, 400)
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
        sy2 = page.evaluate('window.scrollY')
        print(f"Hot-Set scrollY after wheel 600: {sy2} (Expect > 0)")
        assert sy2 > 0, f"Expected Hot-Set scrollY > 0, got {sy2}"

        # Check for card overlap in Hot-Set
        overlap_info = page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('#hotset-grid .skill-card'));
            let overflows = 0;
            cards.slice(0, 20).forEach(c => {
                const rect = c.getBoundingClientRect();
                const bottom = c.querySelector('.card-bottom');
                if (bottom) {
                    const bRect = bottom.getBoundingClientRect();
                    if (bRect.right > rect.right + 2) {
                        overflows++;
                    }
                }
            });
            return { totalCards: cards.length, overflows: overflows };
        }''')
        print("Hot-Set card overlap check:", overlap_info)
        assert overlap_info['overflows'] == 0, f"Detected {overlap_info['overflows']} overflowing cards!"

        # Capture visual screenshot of fixed Hot-Set view
        page.evaluate('window.scrollTo(0, 0)')
        page.wait_for_timeout(200)
        screenshot_path = os.path.join(os.path.dirname(__file__), 'screenshots', 'hotset_fixed_verified.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path)
        print(f"Saved verified screenshot to: {screenshot_path}")

        # 3. Categories View Scroll
        page.evaluate('switchView("categories")')
        page.wait_for_timeout(300)
        page.mouse.move(640, 400)
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
        sy3 = page.evaluate('window.scrollY')
        print(f"Categories scrollY after wheel 600: {sy3} (Expect > 0)")
        assert sy3 > 0, f"Expected Categories scrollY > 0, got {sy3}"

        # 4. Library View Scroll
        page.evaluate('switchView("library")')
        page.wait_for_timeout(300)
        page.mouse.move(640, 400)
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
        sy4 = page.evaluate('window.scrollY')
        print(f"Library scrollY after wheel 600: {sy4} (Expect > 0)")
        assert sy4 > 0, f"Expected Library scrollY > 0, got {sy4}"

        # 5. Guide View Scroll
        page.evaluate('switchView("guide")')
        page.wait_for_timeout(300)
        page.mouse.move(640, 400)
        page.mouse.wheel(0, 600)
        page.wait_for_timeout(300)
        sy5 = page.evaluate('window.scrollY')
        print(f"Guide scrollY after wheel 600: {sy5} (Expect > 0)")
        assert sy5 > 0, f"Expected Guide scrollY > 0, got {sy5}"

        browser.close()
        print("\n🎉 ALL DESKTOP MOUSE SCROLL & LAYOUT TESTS PASSED 100%!")

if __name__ == '__main__':
    test()
