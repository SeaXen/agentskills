# z.ai Dashboard Access Guide

This reference documents how to access z.ai accounts and usage information through browser tools.

## z.ai Website Structure

**Main URL**: `https://z.ai` (also accessible via `https://chat.z.ai/`)

**Key Page Elements**:
- **Login button**: Located in the main navigation bar
- **Value Subscription dialog**: Appears on the main page, promoting paid tiers
- **API Management section**: Available in the footer with links to:
  - API Keys
  - Payment Method
  - Rate Limit

**Navigation Pattern**:
```
z.ai homepage → Login button → Continue with Google → Sign in page → Dashboard
```

## Browser Tool Usage

### Capabilities
- **`browser_navigate`**: Navigate to any z.ai URL
- **`browser_click`**: Click buttons and links by reference ID
- **`browser_snapshot`**: Capture full page structure (useful when vision analysis fails)
- **`browser_vision`**: Analyze page elements (may fail with 429 errors)

### Common Pitfalls

**Vision Analysis Failures**:
- Error: `429 - Insufficient balance or no resource package`
- Workaround: Use `browser_snapshot(full: true)` instead
- Pattern: When vision fails, switch to snapshot-based navigation

**Authentication Requirements**:
- Google OAuth flow requires user interaction
- Cannot fully automate through browser tools
- User must complete the login process manually

**Rate Limiting**:
- Vision analysis can trigger 429 errors
- Multiple rapid snapshots may also hit rate limits
- Use snapshot as fallback when vision is unavailable

## Example Navigation Workflow

```bash
# 1. Navigate to z.ai
browser_navigate('https://z.ai')

# 2. Capture snapshot to identify elements
browser_snapshot(full=true)

# 3. Click login button
browser_click('login_button_ref')

# 4. Handle Google OAuth (user must complete)
browser_snapshot(full=true)

# 5. Navigate to API Management
browser_navigate('https://z.ai/docs/api')  # May return 404
# Alternative: Click through the site navigation
browser_click('api_link_ref')
```

## Checking Provider Limits

**Method 1: Through z.ai Dashboard** (requires login)
1. Complete Google authentication
2. Navigate to dashboard
3. Check usage statistics and rate limits

**Method 2: Direct API Check** (no login required)
```bash
# Check API key info
curl -s https://api.z.ai/api/paas/v4/models \
  -H "Authorization: Bearer $ZAI_API_KEY"
```

**Method 3: Configuration Check**
```bash
# View current config
hermes config
# Look for: model.default, model.provider, model.base_url
```

## Session Notes

- **2026-05-15**: Successfully navigated to z.ai and found login flow
- **Browser tools confirmed**: Navigation and clicking work, but vision analysis can fail with 429 errors
- **Authentication**: Google OAuth requires manual completion
- **Rate limits**: Vision analysis is more likely to hit limits than snapshot-based navigation
