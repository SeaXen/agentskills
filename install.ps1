# AgentSkills One-Click Installer for Windows (PowerShell)
# Usage:
#   irm https://raw.githubusercontent.com/SeaXen/agentskills/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   ⚡ AGENTSKILLS VAULT — ONE-CLICK INSTALLER ⚡" -ForegroundColor Cyan
Write-Host "   Repository: https://github.com/SeaXen/agentskills" -ForegroundColor Gray
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

$targetDir = Join-Path (Get-Location) ".agents"
$repoUrl = "https://github.com/SeaXen/agentskills.git"

# 1. Clone or Pull
if (Test-Path $targetDir) {
    if (Test-Path (Join-Path $targetDir ".git")) {
        Write-Host "📦 Existing .agents vault detected. Pulling latest updates..." -ForegroundColor Yellow
        git -C $targetDir pull origin main
    } else {
        Write-Host "⚠️ Existing .agents directory is not a git repo. Backing up and cloning fresh..." -ForegroundColor Yellow
        $backupDir = ".agents_backup_" + (Get-Date -Format "yyyyMMddHHmmss")
        Rename-Item -Path $targetDir -NewName $backupDir
        git clone $repoUrl $targetDir
    }
} else {
    Write-Host "📥 Cloning complete AgentSkills vault (594 skills, 20 agents, 17 workflows)..." -ForegroundColor Green
    git clone $repoUrl $targetDir
}

if (-not (Test-Path $targetDir)) {
    Write-Host "❌ Installation failed. Please check git and network connection." -ForegroundColor Red
    exit 1
}

# 2. Antigravity IDE / Curated Hot Set Setup (Optional optimization)
$agentDir = Join-Path (Get-Location) ".agent"
Write-Host ""
Write-Host "⚙️ Configuring Antigravity hot-set optimization..." -ForegroundColor Cyan

# Core curated skills list (89 essential skills to avoid token bloat)
$curatedSkills = @(
    "clean-code", "behavioral-modes", "parallel-agents", "architecture",
    "plan-writing", "brainstorming", "app-builder", "antigravity-expert",
    "mcp-builder", "documentation-templates", "i18n-localization",
    "systematic-debugging", "performance-profiling", "grill-me", "codebase-design",
    "vercel-react-best-practices", "nextjs-react-expert", "web-design-guidelines",
    "tailwind-patterns", "frontend-design", "ui-taste", "shadcn", "impeccable",
    "emil-design-eng", "apple-design", "animate", "mobile-design", "ios-design",
    "typescript-expert", "api-patterns", "nodejs-best-practices", "database-design",
    "cloudflare", "workers-best-practices", "wrangler", "testing-patterns",
    "playwright-cli", "caveman-review", "vulnerability-scanner", "powershell-windows"
)

if (Test-Path $agentDir) {
    $hotSkillsDir = Join-Path $agentDir "skills"
    New-Item -ItemType Directory -Force -Path $hotSkillsDir | Out-Null
    
    $copied = 0
    foreach ($s in $curatedSkills) {
        $src = Join-Path $targetDir "skills\$s"
        $dst = Join-Path $hotSkillsDir $s
        if (Test-Path $src) {
            Copy-Item -Recurse -Force -Path $src -Destination $dst
            $copied++
        }
    }
    Write-Host "✓ Synchronized $copied core skills into active hot set (.agent/skills)." -ForegroundColor Green
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "🎉 INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "📁 Full Store (594 Skills):  .agents/skills" -ForegroundColor Gray
Write-Host "🤖 Specialist Agents (20):    .agents/agents" -ForegroundColor Gray
Write-Host "⚡ Workflows (17):            .agents/workflows" -ForegroundColor Gray
Write-Host ""
Write-Host "🔄 How to Update Regularly:" -ForegroundColor Cyan
Write-Host "   - One-click launcher:      .\.agents\update.ps1" -ForegroundColor Yellow
Write-Host "   - Or Git one-liner:        git -C .agents pull" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Green
