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

def run_comprehensive_audit():
    print("=" * 70)
    print("COMPREHENSIVE BROWSER FUNCTIONALITY & MOBILE AUDIT")
    print(f"Target URL: {BASE_URL}")
    print("=" * 70)

    total_passed = 0
    total_failed = 0

    def check(name, condition, extra=""):
        nonlocal total_passed, total_failed
        if condition:
            total_passed += 1
            print(f"  [PASS]: {name} {f'({extra})' if extra else ''}")
        else:
            total_failed += 1
            print(f"  [FAIL]: {name} {f'({extra})' if extra else ''}")

    with sync_playwright() as p:
        # =====================================================================
        # PART 1: MOBILE DEVICE AUDIT (iPhone 14)
        # =====================================================================
        print("\n>>> PART 1: MOBILE DEVICE TEST (iPhone 14, 390x844, Touch Enabled) <<<")
        device = p.devices['iPhone 14']
        browser = p.chromium.launch(headless=True)
        mob_context = browser.new_context(**device)
        mob_page = mob_context.new_page()

        mob_console_errors = []
        mob_page.on('console', lambda m: mob_console_errors.append(m.text) if m.type == 'error' else None)
        mob_page.on('pageerror', lambda e: mob_console_errors.append(str(e)))

        mob_page.goto(BASE_URL, wait_until='networkidle')
        mob_page.wait_for_timeout(300)

        # 1.1 Mobile Touch Scrolling on Skill Hub
        mob_page.mouse.move(180, 250)
        mob_page.mouse.wheel(0, 600)
        mob_page.wait_for_timeout(300)
        scroll_hub = mob_page.evaluate("() => window.scrollY")
        check("Mobile Scroll on Skill Hub Works", scroll_hub > 0, f"scrollY={scroll_hub}")
        mob_page.evaluate("() => window.scrollTo(0, 0)")

        # 1.2 Mobile Bottom Tab Bar Navigation (Touch Taps)
        print("\n[Mobile Tabs & View Switching]")
        # Tap Hot-Set
        mob_page.locator('#mob-tab-hotset').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Tab Tap -> Hot-Set View Active", mob_page.locator('#view-hotset.active').is_visible())
        
        # Mobile Scroll on Hot-Set
        mob_page.mouse.move(180, 300)
        mob_page.mouse.wheel(0, 500)
        mob_page.wait_for_timeout(300)
        scroll_hotset = mob_page.evaluate("() => window.scrollY")
        check("Mobile Scroll on Hot-Set Works", scroll_hotset > 0, f"scrollY={scroll_hotset}")
        mob_page.evaluate("() => window.scrollTo(0, 0)")

        # Tap Categories
        mob_page.locator('#mob-tab-categories').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Tab Tap -> Categories View Active", mob_page.locator('#view-categories.active').is_visible())

        # Mobile Scroll on Categories
        mob_page.mouse.move(180, 300)
        mob_page.mouse.wheel(0, 500)
        mob_page.wait_for_timeout(300)
        scroll_cats = mob_page.evaluate("() => window.scrollY")
        check("Mobile Scroll on Categories Works", scroll_cats > 0, f"scrollY={scroll_cats}")
        mob_page.evaluate("() => window.scrollTo(0, 0)")

        # Tap Library
        mob_page.locator('#mob-tab-library').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Tab Tap -> Library View Active", mob_page.locator('#view-library.active').is_visible())

        # Tap Guide
        mob_page.locator('#mob-tab-guide').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Tab Tap -> Guide View Active", mob_page.locator('#view-guide.active').is_visible())

        # Return to Hub
        mob_page.locator('#mob-tab-skill-hub').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Tab Tap -> Return to Hub Active", mob_page.locator('#view-skill-hub.active').is_visible())

        # 1.3 Mobile Search & Fuzzy Match
        print("\n[Mobile Search & Filtering]")
        search_input = mob_page.locator('#search-input')
        search_input.tap()
        search_input.fill("dokcer")
        mob_page.wait_for_timeout(300)
        first_row = mob_page.locator('#table-body tr:first-child').text_content()
        check("Mobile Fuzzy Search 'dokcer' matches docker-expert", "docker" in first_row.lower())
        
        # Clear filter
        mob_page.locator('.filter-reset-btn').tap()
        mob_page.wait_for_timeout(300)
        check("Mobile Reset Filter Restores Catalog", mob_page.locator('#table-body tr').count() == 50)

        # 1.4 Mobile Category Rail Horizontal Scroll & Tap
        print("\n[Mobile Category Rail]")
        rail_scroll = mob_page.evaluate("""() => {
            const rail = document.getElementById('category-rail');
            rail.scrollLeft = 200;
            return rail.scrollLeft;
        }""")
        check("Category Rail Scrolls Horizontally", rail_scroll >= 150, f"scrollLeft={rail_scroll}")
        first_cat_pill = mob_page.locator('#category-rail .cat-pill:nth-child(2)')
        first_cat_pill.tap()
        mob_page.wait_for_timeout(300)
        check("Category Pill Tap Filters Catalog", mob_page.locator('.filter-chip').count() > 0)
        mob_page.locator('.filter-reset-btn').tap()
        mob_page.wait_for_timeout(300)

        # 1.5 Mobile Detail Drawer (Bottom Sheet) & Tabs
        print("\n[Mobile Detail Drawer Bottom Sheet]")
        first_action_btn = mob_page.locator('#table-body tr:first-child .btn-action')
        first_action_btn.tap()
        mob_page.wait_for_timeout(400)
        drawer_open = mob_page.locator('#drawer-backdrop.open').is_visible()
        check("Drawer Opens on Action Tap", drawer_open)
        
        # Test Prompt Simulator Tab
        mob_page.locator('#tab-drawer-prompts').tap()
        mob_page.wait_for_timeout(300)
        check("Drawer Tab: Prompt Simulator Active", mob_page.locator('#tab-drawer-prompts.active').is_visible())
        
        # Test Live Goal Input in Simulator
        goal_input = mob_page.locator('#prompt-goal-input')
        goal_input.tap()
        goal_input.fill("Automate Docker container deployments")
        mob_page.wait_for_timeout(200)
        code_box_text = mob_page.locator('.prompt-code-box').first.text_content()
        check("Live Simulator Updates Goal on Mobile", "Automate Docker container deployments" in code_box_text)

        # Close Drawer
        mob_page.locator('#drawer-close-btn').tap()
        mob_page.wait_for_timeout(300)
        check("Drawer Closes on Tap", not mob_page.locator('#drawer-backdrop.open').is_visible())

        # 1.6 Mobile Agent Stack Builder Tray
        print("\n[Mobile Agent Stack Builder]")
        # Tap + Stack on first item
        mob_page.locator('#table-body tr:first-child .btn-stack-toggle').tap()
        mob_page.wait_for_timeout(200)
        badge = mob_page.locator('#stack-count-badge').text_content()
        check("Stack Badge Incremented on Tap", badge == "1", f"badge={badge}")

        # Tap dock to expand
        mob_page.locator('#stack-tray-dock').tap()
        mob_page.wait_for_timeout(300)
        check("Stack Tray Expands on Tap", mob_page.locator('#agent-stack-tray.expanded').is_visible())

        # Tap batch symlink copy
        mob_page.locator('#btn-stack-link').tap()
        mob_page.wait_for_timeout(200)
        toast_text = mob_page.locator('#toast').text_content()
        check("Batch Symlink Copied with Toast", "python .agents/library/activate_skill.py link" in toast_text, f"Toast: {toast_text}")

        # Clear Stack
        mob_page.locator('.stack-panel-actions .pill-danger').tap()
        mob_page.wait_for_timeout(200)
        check("Stack Cleared on Tap", mob_page.locator('#stack-count-badge').text_content() == "0")

        # Collapse Tray
        mob_page.locator('#stack-tray-dock').tap()
        mob_page.wait_for_timeout(200)

        # 1.8 Mobile Theme Switcher
        print("\n[Mobile Theme Switcher]")
        init_theme = mob_page.evaluate("() => document.documentElement.getAttribute('data-theme') || 'light'")
        mob_page.locator('#theme-toggle').tap()
        mob_page.wait_for_timeout(200)
        new_theme = mob_page.evaluate("() => document.documentElement.getAttribute('data-theme')")
        check("Theme Switches on Tap", new_theme != init_theme, f"Switched to {new_theme}")
        mob_page.locator('#theme-toggle').tap()
        mob_page.wait_for_timeout(200)

        # 1.9 Mobile Console Errors
        check("Zero Mobile Console Errors", len(mob_console_errors) == 0, f"Errors: {mob_console_errors}")

        mob_context.close()

        # =====================================================================
        # PART 2: DESKTOP AUDIT (1440x900)
        # =====================================================================
        print("\n>>> PART 2: DESKTOP WORKBENCH TEST (1440x900) <<<")
        desk_context = browser.new_context(viewport={'width': 1440, 'height': 900})
        desk_page = desk_context.new_page()

        desk_console_errors = []
        desk_page.on('console', lambda m: desk_console_errors.append(m.text) if m.type == 'error' else None)
        desk_page.on('pageerror', lambda e: desk_console_errors.append(str(e)))

        desk_page.goto(BASE_URL, wait_until='networkidle')
        desk_page.wait_for_timeout(300)

        # 2.1 Desktop Mouse Wheel Scroll
        desk_page.mouse.move(640, 400)
        desk_page.mouse.wheel(0, 500)
        desk_page.wait_for_timeout(200)
        desk_scroll = desk_page.evaluate("() => window.scrollY")
        check("Desktop Mouse Wheel Scrolling Functional", desk_scroll > 0, f"scrollY={desk_scroll}")
        desk_page.evaluate("() => window.scrollTo(0, 0)")

        # 2.2 Desktop Side-by-Side Comparator Modal
        print("\n[Desktop Comparator Modal]")
        desk_page.locator('#view-grid-btn').click()
        desk_page.wait_for_timeout(200)
        desk_page.locator('.skill-card:nth-child(1) button[aria-label^="Compare"]').click()
        desk_page.wait_for_timeout(200)
        desk_page.locator('.skill-card:nth-child(2) button[aria-label^="Compare"]').click()
        desk_page.wait_for_timeout(400)
        check("Comparator Modal Opens on 2 Skills Selected", desk_page.locator('#comparator-backdrop.open').is_visible())
        cols = desk_page.locator('.comparator-matrix-table tr:first-child th').count()
        check("Comparator Matrix Table Has 3 Columns", cols == 3, f"cols={cols}")
        desk_page.locator('#comparator-close-btn').click()
        desk_page.wait_for_timeout(200)
        check("Comparator Modal Closes on Close Button Click", not desk_page.locator('#comparator-backdrop.open').is_visible())
        desk_page.locator('#view-table-btn').click()
        desk_page.wait_for_timeout(200)

        # 2.3 Desktop Category Quick Actions
        print("\n[Desktop Category Quick Actions]")
        desk_page.locator('#tab-categories').click()
        desk_page.wait_for_timeout(300)
        first_cat_actions = desk_page.locator('.cat-dir-card:first-child .cat-quick-actions')
        check("Category Card Quick Actions Present", first_cat_actions.is_visible())
        first_cat_link_btn = desk_page.locator('.cat-dir-card:first-child .cat-quick-btn-primary')
        first_cat_link_btn.click()
        desk_page.wait_for_timeout(200)
        cat_toast = desk_page.locator('#toast-message').text_content()
        check("Category Link All Copies Command", "python .agents/library/activate_skill.py link-category" in cat_toast, f"Toast: {cat_toast}")

        # 2.4 Desktop Pagination Navigation
        print("\n[Desktop Pagination]")
        desk_page.locator('#tab-skill-hub').click()
        desk_page.wait_for_timeout(300)
        check("Page 1 Next Button Enabled", not desk_page.locator('#next-page-btn').is_disabled())
        desk_page.locator('#next-page-btn').click()
        desk_page.wait_for_timeout(200)
        info_text = desk_page.locator('#page-indicator').text_content()
        check("Advanced to Page 2", "Page 2" in info_text, f"Got: {info_text}")
        desk_page.locator('#prev-page-btn').click()
        desk_page.wait_for_timeout(200)
        check("Returned to Page 1", "Page 1" in desk_page.locator('#page-indicator').text_content())

        # 2.5 Desktop View Toggle (Grid / Table)
        print("\n[Desktop View Toggles]")
        desk_page.locator('#view-grid-btn').click()
        desk_page.wait_for_timeout(200)
        check("Grid View Active", desk_page.locator('#grid-container').is_visible())
        check("Table View Hidden", not desk_page.locator('#table-container').is_visible())
        desk_page.locator('#view-table-btn').click()
        desk_page.wait_for_timeout(200)
        check("Table View Restored", desk_page.locator('#table-container').is_visible())

        # 2.6 Desktop 1-Click Install Mode Switcher
        print("\n[Desktop 1-Click Install Mode Switcher]")
        first_cmd_box = desk_page.locator('#table-body tr:first-child .cmd-box code')
        desk_page.locator('.cmd-type-btn[data-mode="python"]').click()
        desk_page.wait_for_timeout(200)
        py_cmd = first_cmd_box.text_content()
        check("Switched to Python Activation Mode", "python .agents/library/activate_skill.py" in py_cmd, f"Cmd: {py_cmd}")
        desk_page.locator('.cmd-type-btn[data-mode="myrepo"]').click()
        desk_page.wait_for_timeout(200)
        myrepo_cmd = first_cmd_box.text_content()
        check("Switched to My Repo Mode", "SeaXen/agentskills" in myrepo_cmd, f"Cmd: {myrepo_cmd}")
        desk_page.locator('.cmd-type-btn[data-mode="npx"]').click()
        desk_page.wait_for_timeout(200)

        # 2.7 Desktop Console Errors
        check("Zero Desktop Console Errors", len(desk_console_errors) == 0, f"Errors: {desk_console_errors}")

        desk_context.close()
        browser.close()

    print("\n" + "=" * 70)
    print(f"AUDIT SUMMARY: {total_passed} PASSED, {total_failed} FAILED")
    print("=" * 70)

    if total_failed == 0:
        print(">>> ALL BROWSER FUNCTIONS VERIFIED WORKING 100%! <<<")
    else:
        print(">>> SOME CHECKS FAILED! <<<")
        sys.exit(1)

if __name__ == '__main__':
    run_comprehensive_audit()
