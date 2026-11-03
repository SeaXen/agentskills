# Pattern: Giant Inline Script in Next.js Page

## Observed in
- `/mnt/tb/1Apps/pyhox/app/page.tsx` (969+ lines, mostly one massive template literal containing the entire app logic + repeated JSX strings)

## Key Problems Encountered
- `patch` repeatedly failed with "Escape-drift detected" because the giant string literal contained `\"` sequences.
- Short repeated strings (e.g. "Live Watchlist" card JSX) matched multiple times (once in real JSX, many times inside the script string).
- User wanted compact UI + working buttons + live verification.

## Recommended Approach for This Pattern
1. Do **not** attempt many small patches on the giant string.
2. Use very long, unique surrounding context for any necessary patch.
3. Prefer adding new React components outside the monolith when possible.
4. For button/feature additions, extend the existing `bind()` function and add minimal JSX in a safe location.
5. Always verify with `npm run dev` + browser tools after changes.

## Lesson
When a file exceeds ~600-700 lines and contains embedded large strings, the cost of patching rises dramatically. Consider whether the next improvement should be a structural refactor instead of continued string surgery.
