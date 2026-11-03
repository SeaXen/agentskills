# Notion MCP: Page Not Shared with Integration

## Problem
When calling Notion MCP tools (e.g., `mcp_notion_get_page`), you get:
- `403 Forbidden`
- `Connection not found`
- `Error: Notion API error: 403`

## Root Cause
The **Notion page/database is not shared with your integration**. Notion requires **explicit sharing** for API access, even if you own the page.

## Fix
### Step 1: Share the Page with Your Integration
1. Open the Notion page in your browser: [https://app.notion.com/p/searex/Hermes-37a5588e846f8081b37df1bd6436b3fa](https://app.notion.com/p/searex/Hermes-37a5588e846f8081b37df1bd6436b3fa)
2. Click **Share** (top-right).
3. Under **Invite a person**, search for your **integration name** (e.g., "Hermes" or the name you gave it when creating the token).
4. Click **Allow full access** (read/write).

### Step 2: Verify Sharing
- The integration should now appear in the **Share** dialog with a checkmark.
- If you don’t see it, refresh the page and try again.

### Step 3: Retry the MCP Tool Call
Once shared, retry the tool call in Hermes (e.g., `mcp_notion_get_page`). It should now work.

## Verification via API
To confirm the page is accessible via the Notion API:

```bash
curl -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  "https://api.notion.com/v1/pages/Hermes-37a5588e846f8081b37df1bd6436b3fa"
```

**Expected Output:**
- A JSON response with the page details.

**If you get `403`:**
- The page is **not shared** with your integration.
- Double-check the **integration name** and **page sharing settings**.

## Common Mistakes
1. **Using a Personal Token Instead of an Integration Token**
   - Notion **requires an integration token** (starts with `ntn_`) for API access.
   - Personal tokens (from `Settings & Members` → `Integrations` → `Internal Integration Token`) **do not work** for most API endpoints.

2. **Not Sharing the Page with the Integration**
   - Even with a valid token, the **page must be explicitly shared** with the integration.

3. **Using the Wrong Page ID**
   - The page ID is the **last part of the URL** (e.g., `Hermes-37a5588e846f8081b37df1bd6436b3fa` in `https://app.notion.com/p/searex/Hermes-37a5588e846f8081b37df1bd6436b3fa`).
   - **Do not** include the workspace name (`searex`) or URL prefix.

## Troubleshooting
### 1. Check Your Integration Token
- Go to: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
- Verify your integration exists and the token is correct.
- **Regenerate the token** if unsure.

### 2. Check Page Sharing
- Open the page in Notion.
- Click **Share** → **Invite a person** → Search for your integration.
- If it doesn’t appear, the integration may not have been created correctly.

### 3. Test with a Public Page
- Try accessing a **public Notion page** (e.g., a page with **Share to web** enabled).
- If this works, the issue is **sharing permissions** on your private page.

### 4. Check Notion API Status
- Visit: [https://status.notion.so](https://status.notion.so)
- Ensure the API is **operational**.

## Best Practices
1. **Use a Dedicated Integration**
   - Create a **separate integration** for Hermes (e.g., "Hermes Agent").
   - Avoid reusing integrations across multiple tools.

2. **Share at the Workspace Level**
   - For broad access, share the **entire workspace** with the integration.
   - Go to **Settings & Members** → **Integrations** → Select your integration → **Share all pages**.

3. **Use Environment Variables for Tokens**
   - Store `NOTION_TOKEN` in **Bitwarden** or a **secure `.env` file**.
   - **Never** commit tokens to Git.

4. **Test with `mcp_notion_get_page` First**
   - Before writing/updating, verify **read access** with `mcp_notion_get_page`.

## Example: Full Workflow
1. **Create Integration**
   - Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) → **Create new integration** → Name it "Hermes Agent" → Copy the token.

2. **Share the Page**
   - Open [Hermes-37a5588e846f8081b37df1bd6436b3fa](https://app.notion.com/p/searex/Hermes-37a5588e846f8081b37df1bd6436b3fa) → **Share** → **Invite a person** → Search for "Hermes Agent" → **Allow full access**.

3. **Configure Hermes**
   - Add to `~/.hermes/config.yaml`:
     ```yaml
     mcp_servers:
       notion:
         command: "/root/.hermes/scripts/mcp-notion.sh"
         enabled: true
     ```
   - Ensure `/root/.hermes/scripts/mcp-notion.sh` exports `NOTION_TOKEN`.

4. **Restart Hermes**
   ```bash
   hermes restart
   ```

5. **Test the Tool**
   - Call `mcp_notion_get_page` with the page ID.

## References
- [Notion Integration Tokens](https://www.notion.so/my-integrations)
- [Notion API Docs](https://developers.notion.com/docs)
- [Notion MCP Server](https://github.com/notionhq/notion-mcp-server)