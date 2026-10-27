#!/usr/bin/env bash
# AgentSkills One-Click Installer for macOS & Linux
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash

set -e

echo ""
echo "=========================================================="
echo "   ⚡ AGENTSKILLS VAULT — ONE-CLICK INSTALLER ⚡"
echo "   Repository: https://github.com/SeaXen/agentskills"
echo "=========================================================="
echo ""

TARGET_DIR="$(pwd)/.agents"
REPO_URL="https://github.com/SeaXen/agentskills.git"

if [ -d "$TARGET_DIR" ]; then
    if [ -d "$TARGET_DIR/.git" ]; then
        echo "📦 Existing .agents vault detected. Pulling latest updates..."
        git -C "$TARGET_DIR" pull origin main
    else
        echo "⚠️ Existing .agents directory is not a git repo. Backing up and cloning fresh..."
        BACKUP_DIR=".agents_backup_$(date +%Y%m%d%H%M%S)"
        mv "$TARGET_DIR" "$BACKUP_DIR"
        git clone "$REPO_URL" "$TARGET_DIR"
    fi
else
    echo "📥 Cloning complete AgentSkills vault (594 skills, 20 agents, 17 workflows)..."
    git clone "$REPO_URL" "$TARGET_DIR"
fi

# Optional Antigravity hot set setup
AGENT_DIR="$(pwd)/.agent"
if [ -d "$AGENT_DIR" ]; then
    echo ""
    echo "⚙️ Configuring Antigravity hot-set optimization..."
    mkdir -p "$AGENT_DIR/skills"
    CURATED=("clean-code" "behavioral-modes" "parallel-agents" "architecture" "plan-writing" "brainstorming" "app-builder" "antigravity-expert" "mcp-builder" "documentation-templates" "i18n-localization" "systematic-debugging" "performance-profiling" "grill-me" "codebase-design" "vercel-react-best-practices" "nextjs-react-expert" "web-design-guidelines" "tailwind-patterns" "frontend-design" "ui-taste" "shadcn" "impeccable" "emil-design-eng" "apple-design" "animate" "mobile-design" "ios-design" "typescript-expert" "api-patterns" "nodejs-best-practices" "database-design" "cloudflare" "workers-best-practices" "wrangler" "testing-patterns" "playwright-cli" "caveman-review" "vulnerability-scanner" "bash-linux")
    COPIED=0
    for s in "${CURATED[@]}"; do
        if [ -d "$TARGET_DIR/skills/$s" ]; then
            cp -r "$TARGET_DIR/skills/$s" "$AGENT_DIR/skills/"
            COPIED=$((COPIED + 1))
        fi
    done
    echo "✓ Synchronized $COPIED core skills into active hot set (.agent/skills)."
fi

echo ""
echo "=========================================================="
echo "🎉 INSTALLATION COMPLETE!"
echo "=========================================================="
echo "📁 Full Store (594 Skills):  .agents/skills"
echo "🤖 Specialist Agents (20):    .agents/agents"
echo "⚡ Workflows (17):            .agents/workflows"
echo ""
echo "🔄 How to Update Regularly:"
echo "   - Master update script:    python .agents/update.py"
echo "   - Or Git one-liner:        git -C .agents pull"
echo "=========================================================="
