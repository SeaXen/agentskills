import os
import sys
import time

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:8080')
ARTIFACT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'screenshots'))
os.makedirs(ARTIFACT_DIR, exist_ok=True)

def run_tests():
    print("====================================================")
    print("Starting Skill.Sea WebApp Playwright Test Suite")
    print(f"Target URL: {BASE_URL}")
    print("====================================================")

    console_errors = []
    page_errors = []
    test_results = []

    def record(name, passed, details=""):
        status = "[PASS]" if passed else "[FAIL]"
        test_results.append((name, passed, details))
        print(f"  {status}: {name} {f'({details})' if details else ''}")
        if not passed:
            print(f"    ERROR DETAILS: {details}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        # Grant clipboard permissions for 1-click install testing
        context.grant_permissions(['clipboard-read', 'clipboard-write'])
        page = context.new_page()

        # Capture console and page errors
        page.on('console', lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ['error', 'warning'] else None)
        page.on('pageerror', lambda err: page_errors.append(str(err)))

        # -----------------------------------------------------------------
        # TEST 1: Initial Page Load & Semantic Landmarks
        # -----------------------------------------------------------------
        print("\n[Suite 1] Initial Page Load & Semantic Landmarks")
        response = page.goto(BASE_URL, wait_until='networkidle')
        record("HTTP Status 200", response.status == 200, f"Status: {response.status}")
        
        title = page.title()
        record("Page Title Contains Skill.Sea", "Skill.Sea" in title, f"Title: '{title}'")

        skip_link = page.locator('a.skip-link')
        record("Accessible Skip Link Exists", skip_link.count() == 1, "a.skip-link found")

        main_landmark = page.locator('main#main-content')
        record("Main Landmark #main-content Present", main_landmark.count() == 1)

        # -----------------------------------------------------------------
        # TEST 2: Metrics Telemetry Verification
        # -----------------------------------------------------------------
        print("\n[Suite 2] Telemetry Metrics Tiles")
        page.wait_for_selector('#stat-total-skills')
        skills_text = page.locator('#stat-total-skills').text_content()
        cats_text = page.locator('#stat-total-cats').text_content()
        repos_text = page.locator('#stat-total-repos').text_content()
        hot_text = page.locator('#stat-active-hot').text_content()

        record("Total Skills Metric 6,063", skills_text == "6,063", f"Got: {skills_text}")
        record("Total Categories Metric 38", cats_text == "38", f"Got: {cats_text}")
        record("Total Repositories Metric 210", repos_text == "210", f"Got: {repos_text}")
        record("Active Hot-Set Metric 130", hot_text == "130", f"Got: {hot_text}")

        # -----------------------------------------------------------------
        # TEST 3: Catalog Table Populated & Tabular Numerals
        # -----------------------------------------------------------------
        print("\n[Suite 3] Catalog Table & Numerals")
        page.wait_for_selector('#table-body tr')
        row_count = page.locator('#table-body tr').count()
        record("Catalog Table Rows Rendered", row_count > 10, f"Rows on Page 1: {row_count}")

        first_rank = page.locator('#table-body tr:first-child .rank-pill').text_content()
        record("First Skill Has Rank #1", first_rank.strip() == "1", f"Got: {first_rank}")

        # -----------------------------------------------------------------
        # TEST 4: Search & Realtime Filter Chips
        # -----------------------------------------------------------------
        print("\n[Suite 4] Search Filtering & Accessible Chips")
        search_input = page.locator('#search-input')
        search_input.fill("python")
        page.wait_for_timeout(300) # Wait for 150ms debounce

        chip = page.locator('#active-filters-bar .filter-chip')
        record("Active Filter Chip Rendered", chip.count() > 0, "Search chip visible")

        remove_btn = page.locator('#active-filters-bar .filter-chip-remove')
        record("Remove Filter Chip Button Present", remove_btn.count() > 0)
        
        # Click remove button
        remove_btn.first.click()
        page.wait_for_timeout(300)
        record("Filter Chip Removed on Click", page.locator('#active-filters-bar').is_hidden())

        # -----------------------------------------------------------------
        # TEST 5: Category Dropdown Filtering
        # -----------------------------------------------------------------
        print("\n[Suite 5] Category Selection & Filtering")
        cat_select = page.locator('#category-filter-select')
        cat_select.select_option('code-quality-refactoring')
        page.wait_for_timeout(300)

        item_count_text = page.locator('#item-count').text_content()
        record("Filtered by Category", "skills" in item_count_text, f"Item count: {item_count_text}")

        reset_btn = page.locator('.filter-reset-btn')
        if reset_btn.is_visible():
            reset_btn.click()
            page.wait_for_timeout(300)
        record("Reset All Filters Restores Catalog", page.locator('#category-filter-select').input_value() == "all")

        # -----------------------------------------------------------------
        # TEST 6: 1-Click Command Mode Toggle (NPX / Python / My Repo)
        # -----------------------------------------------------------------
        print("\n[Suite 6] 1-Click Install Command Mode Switcher")
        first_cmd_box = page.locator('#table-body tr:first-child .cmd-box code')
        initial_cmd = first_cmd_box.text_content()
        record("Default Mode is Universal NPX", "npx skills add" in initial_cmd, f"Cmd: {initial_cmd}")

        # Switch to Python mode
        py_btn = page.locator('.cmd-type-btn[data-mode="python"]')
        py_btn.click()
        page.wait_for_timeout(200)
        py_cmd = first_cmd_box.text_content()
        record("Switched to Python Activation Mode", "python .agents/library/activate_skill.py" in py_cmd, f"Cmd: {py_cmd}")

        # Switch to My Repo mode
        myrepo_btn = page.locator('.cmd-type-btn[data-mode="myrepo"]')
        myrepo_btn.click()
        page.wait_for_timeout(200)
        myrepo_cmd = first_cmd_box.text_content()
        record("Switched to My Repo Mode", "SeaXen/agentskills" in myrepo_cmd, f"Cmd: {myrepo_cmd}")

        # Reset back to NPX
        page.locator('.cmd-type-btn[data-mode="npx"]').click()
        page.wait_for_timeout(200)

        # -----------------------------------------------------------------
        # TEST 7: View Toggles (Table vs Grid)
        # -----------------------------------------------------------------
        print("\n[Suite 7] View Toggles (Table / Grid)")
        page.locator('#view-grid-btn').click()
        page.wait_for_timeout(200)
        record("Grid Container Visible", page.locator('#grid-container').is_visible())
        record("Table Container Hidden", not page.locator('#table-container').is_visible())

        page.locator('#view-table-btn').click()
        page.wait_for_timeout(200)
        record("Table Container Restored", page.locator('#table-container').is_visible())

        # -----------------------------------------------------------------
        # TEST 8: Pagination Controls
        # -----------------------------------------------------------------
        print("\n[Suite 8] Pagination Navigation")
        prev_btn = page.locator('#prev-page-btn')
        next_btn = page.locator('#next-page-btn')
        page_indicator = page.locator('#page-indicator')

        record("Previous Button Disabled on Page 1", prev_btn.is_disabled())
        record("Next Button Enabled on Page 1", not next_btn.is_disabled())
        
        next_btn.click()
        page.wait_for_timeout(300)
        record("Advanced to Page 2", "Page 2" in page_indicator.text_content(), f"Got: {page_indicator.text_content()}")
        record("Previous Button Now Enabled", not prev_btn.is_disabled())

        prev_btn.click()
        page.wait_for_timeout(300)
        record("Returned to Page 1", "Page 1" in page_indicator.text_content())

        # -----------------------------------------------------------------
        # TEST 9: SPA Navigation (Hot-Set, Categories, Library, Guide)
        # -----------------------------------------------------------------
        print("\n[Suite 9] SPA Tab Page Views")
        # 9.1 Hot-Set
        page.locator('#tab-hotset').click()
        page.wait_for_timeout(200)
        record("Hot-Set View Active", page.locator('#view-hotset').is_visible())
        record("Hot-Set Cards Rendered", page.locator('#hotset-grid .skill-card').count() >= 100)

        # 9.2 Categories
        page.locator('#tab-categories').click()
        page.wait_for_timeout(200)
        record("Categories View Active", page.locator('#view-categories').is_visible())
        record("38 Category Cards Rendered", page.locator('#category-directory-grid .cat-dir-card').count() == 38)

        # 9.3 Library Repositories
        page.locator('#tab-library').click()
        page.wait_for_timeout(200)
        record("Library View Active", page.locator('#view-library').is_visible())
        record("210 Repository Cards Rendered", page.locator('#repo-grid .repo-card').count() == 210)

        # 9.4 Guide
        page.locator('#tab-guide').click()
        page.wait_for_timeout(200)
        record("Guide View Active", page.locator('#view-guide').is_visible())
        record("Guide Cards Present", page.locator('.guide-card').count() >= 4)

        # Return to Hub
        page.locator('#tab-skill-hub').click()
        page.wait_for_timeout(200)
        record("Returned to Skill Hub", page.locator('#view-skill-hub').is_visible())

        # -----------------------------------------------------------------
        # TEST 10: Slide-Over Detail Drawer & Keyboard Dismissal
        # -----------------------------------------------------------------
        print("\n[Suite 10] Slide-Over Drawer & Accessibility")
        inspect_btn = page.locator('#table-body tr:first-child .btn-action')
        inspect_btn.click()
        page.wait_for_timeout(300)

        drawer = page.locator('#drawer-backdrop')
        record("Drawer Opens with .open class", drawer.evaluate('el => el.classList.contains("open")'))
        record("Drawer Has aria-hidden=false", drawer.get_attribute('aria-hidden') == "false")
        record("Drawer Has role=dialog", drawer.get_attribute('role') == "dialog")
        record("Drawer Has aria-modal=true", drawer.get_attribute('aria-modal') == "true")
        
        drawer_title = page.locator('#drawer-title').text_content()
        record("Drawer Title Populated", len(drawer_title.strip()) > 0, f"Title: {drawer_title}")

        # Press Escape key to dismiss
        page.keyboard.press('Escape')
        page.wait_for_timeout(300)
        record("Drawer Closes on Escape Key", not drawer.evaluate('el => el.classList.contains("open")'))
        record("Drawer Sets aria-hidden=true", drawer.get_attribute('aria-hidden') == "true")

        # -----------------------------------------------------------------
        # TEST 11: Dark & Light Mode Toggle
        # -----------------------------------------------------------------
        print("\n[Suite 11] Theme Toggling (Dark/Light)")
        initial_theme = page.locator('html').get_attribute('data-theme') or 'light'
        expected_next = 'dark' if initial_theme == 'light' else 'light'
        record("Initial Theme Identified", initial_theme in ['light', 'dark'], f"Initial: {initial_theme}")

        # Click theme toggle button
        page.locator('#theme-toggle').click()
        page.wait_for_timeout(200)
        toggled_theme = page.locator('html').get_attribute('data-theme')
        record("Theme Toggled via Click", toggled_theme == expected_next, f"Switched to: {toggled_theme}")

        # Press 'T' keyboard shortcut to toggle back
        page.keyboard.press('t')
        page.wait_for_timeout(200)
        restored_theme = page.locator('html').get_attribute('data-theme')
        record("Theme Toggled back via 'T' Key", restored_theme == initial_theme, f"Restored to: {restored_theme}")

        # -----------------------------------------------------------------
        # TEST 12: Screenshots (Desktop & Mobile)
        # -----------------------------------------------------------------
        print("\n[Suite 12] Responsive Breakpoints & Screenshot Capture")
        desktop_path = os.path.join(ARTIFACT_DIR, 'desktop_e2e_verified.png')
        page.screenshot(path=desktop_path, full_page=False)
        record("Captured Desktop Viewport Screenshot", os.path.exists(desktop_path), f"Saved to {desktop_path}")

        # Switch to Mobile Viewport (iPhone / Android spec: 375x667)
        page.set_viewport_size({'width': 375, 'height': 667})
        page.wait_for_timeout(300)
        record("Mobile Tab Bar Visible on Mobile", page.locator('.mobile-tab-bar').is_visible())
        
        mobile_path = os.path.join(ARTIFACT_DIR, 'mobile_e2e_verified.png')
        page.screenshot(path=mobile_path, full_page=False)
        record("Captured Mobile Viewport Screenshot", os.path.exists(mobile_path), f"Saved to {mobile_path}")

        # -----------------------------------------------------------------
        # TEST 13: Console & Runtime Errors
        # -----------------------------------------------------------------
        print("\n[Suite 13] Browser Runtime Errors")
        record("Zero Browser Uncaught Exceptions", len(page_errors) == 0, f"Errors: {page_errors}")
        severe_errors = [e for e in console_errors if '[error]' in e]
        record("Zero Browser Console Severe Errors", len(severe_errors) == 0, f"Console Errors: {severe_errors}")

        browser.close()

    # Final summary report
    print("\n====================================================")
    total_tests = len(test_results)
    passed_tests = sum(1 for _, p, _ in test_results if p)
    failed_tests = total_tests - passed_tests

    print(f"Results: {passed_tests}/{total_tests} Tests Passed")
    print(f"====================================================")
    if failed_tests > 0:
        print(f"[FAIL] {failed_tests} tests failed!")
        sys.exit(1)
    else:
        print(">>> ALL PLAYWRIGHT E2E TESTS PASSED WITH 100% SUCCESS! <<<")
        sys.exit(0)

if __name__ == '__main__':
    run_tests()
