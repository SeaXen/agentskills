# Check if all phases in task_plan.md are complete
# Default invocation: advisory echo, always exits 0 (Stop hook status report).
# With -Validate: read-only creation check; exits 1 for an untrackable plan.
# With -Gate: deliberate completion gate, opt-in per plan via <plan-dir>/.mode.
# Used by Stop hook to report task completion status.
#
# Gate mode (v3, -Gate flag) blocks ONLY when ALL hold (design "Gate decision table"):
#   1. <plan-dir>/.mode exists and contains "gate" (explicit opt-in)
#   2. an in_progress phase exists (not merely complete<total)
#   3. the Stop hook input JSON on stdin does not set stop_hook_active=true
#   4. the block counter (<plan-dir>/.stop_blocks) is below cap (PWF_GATE_CAP, default 20)
#   5. the ledger advanced since the last block (stall -> allow stop)
# When all hold, emits a single-line block-decision JSON on stdout and exits 0.
# Otherwise reports incomplete plans and exits 0; completed plans stay silent
# with -Gate, including legacy plans without .mode. Explicit reports are unchanged.
#
# Stdin: read only when input is redirected ([Console]::IsInputRedirected), so an
# interactive console never blocks. Hook-piped JSON is EOF-terminated.

param(
    [string]$PlanFile = "",
    [switch]$Gate,
    [switch]$Validate
)

# issue #195: per-invocation opt-out (PLANNING_DISABLED=1) for one-shot/CI
# sessions that share a cwd with a plan but never opted into it.
if ($env:PLANNING_DISABLED -eq '1' -and -not $Validate) { exit 0 }

if ($PlanFile -ne "") {
    $PlanDir = Split-Path -Parent $PlanFile
    if ($PlanDir -eq "") { $PlanDir = "." }
} else {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $resolver = Join-Path $scriptDir "resolve-plan-dir.ps1"
    $resolvedDir = ""
    if (Test-Path $resolver) {
        try {
            $resolvedDir = (& $resolver 2>$null | Select-Object -First 1)
            if ($null -eq $resolvedDir) { $resolvedDir = "" }
            if (-not $resolvedDir -and ((& $resolver -CheckAmbiguity) -eq "PWF_PLAN_AMBIGUOUS_V1")) {
                if ($Validate) { Write-Output '[planning-with-files] Plan format invalid: select one plan before validation.'; exit 1 }
                exit 0
            }
        } catch {
            $resolvedDir = ""
        }
    }
    if ($resolvedDir -ne "" -and (Test-Path (Join-Path $resolvedDir "task_plan.md"))) {
        $PlanFile = Join-Path $resolvedDir "task_plan.md"
        $PlanDir = $resolvedDir
    } else {
        if ($Validate -and ($env:PLAN_ID -or $env:PWF_PLAN_ROOT)) {
            Write-Output '[planning-with-files] Plan format invalid: an explicit plan selector did not resolve.'
            exit 1
        }
        $PlanFile = "task_plan.md"
        $PlanDir = "."
    }
}

if (-not (Test-Path $PlanFile)) {
    if ($Validate) { Write-Output '[planning-with-files] Plan format invalid: task_plan.md was not found.'; exit 1 }
    # Automatic gate checks have nothing to report without a plan; the explicit report keeps its notice.
    if ($Gate) { exit 0 }
    Write-Host '[planning-with-files] No task_plan.md found -- no active planning session.'
    exit 0
}

# Read file content
$content = Get-Content $PlanFile -Raw

# Explicit creation validation never mutates a plan or changes Stop behavior.
if ($Validate) {
    $phases = 0
    $statuses = 0
    $inPhase = $false
    $invalid = $false
    foreach ($line in ($content -split '\r?\n')) {
        if ($line -cmatch '^### Phase(?:[ \t]|$)') {
            if ($inPhase -and $statuses -ne 1) { $invalid = $true }
            $phases++
            $inPhase = $true
            $statuses = 0
        } elseif ($line -match '^#{1,3}[ \t]') {
            if ($inPhase -and $statuses -ne 1) { $invalid = $true }
            $inPhase = $false
        }
        if ($inPhase) {
            $statuses += ([regex]::Matches($line, '\*\*Status:\*\*[ \t]+(?:pending|in_progress|complete)(?:[^\p{L}\p{N}_]|$)')).Count
            $statuses += ([regex]::Matches($line, '\[(?:pending|in_progress|complete)\]')).Count
        }
    }
    if ($inPhase -and $statuses -ne 1) { $invalid = $true }
    if ($phases -eq 0 -or $invalid) {
        Write-Output '[planning-with-files] Plan format invalid: use ### Phase headings with exactly one native status per phase.'
        exit 1
    }
    Write-Output ('[planning-with-files] Plan format valid (' + $phases + ' phases).')
    exit 0
}

# Count total phases
$TOTAL = ([regex]::Matches($content, "### Phase")).Count

# Count both formats per field and keep the larger of the two. A plan may mix
# '**Status:** pending' on one phase with '[in_progress]' on another; counting
# only the primary format (and falling back to inline ONLY when all three
# primaries are zero) lost the inline count and let an in_progress plan slip
# past the gate. Per-field max preserves the legacy single-format result
# (the other format contributes 0) while catching mixed plans.
$completePrimary = ([regex]::Matches($content, "\*\*Status:\*\* complete")).Count
$inProgressPrimary = ([regex]::Matches($content, "\*\*Status:\*\* in_progress")).Count
$pendingPrimary = ([regex]::Matches($content, "\*\*Status:\*\* pending")).Count

$completeInline = ([regex]::Matches($content, "\[complete\]")).Count
$inProgressInline = ([regex]::Matches($content, "\[in_progress\]")).Count
$pendingInline = ([regex]::Matches($content, "\[pending\]")).Count

$COMPLETE = [Math]::Max($completePrimary, $completeInline)
$IN_PROGRESS = [Math]::Max($inProgressPrimary, $inProgressInline)
$PENDING = [Math]::Max($pendingPrimary, $pendingInline)

# issue #191: no "### Phase" headings -> not a phase-structured plan. Report
# nothing rather than a false "0/0 phases complete" status. With TOTAL=0 the
# gate can never legitimately block (IN_PROGRESS is also 0), so exit is safe.
if ($TOTAL -eq 0) {
    exit 0
}

# Keep explicit reports, but omit routine success from automatic gate checks.
function Write-AdvisoryReport {
    if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
        if ($Gate) { return }
        Write-Host ('[planning-with-files] ALL PHASES COMPLETE (' + $COMPLETE + '/' + $TOTAL + '). If the user has additional work, add new phases to task_plan.md before starting.')
    } else {
        Write-Host ('[planning-with-files] Task in progress (' + $COMPLETE + '/' + $TOTAL + ' phases complete). Update progress.md before stopping.')
        if ($IN_PROGRESS -gt 0) {
            Write-Host ('[planning-with-files] ' + $IN_PROGRESS + ' phase(s) still in progress.')
        }
        if ($PENDING -gt 0) {
            Write-Host ('[planning-with-files] ' + $PENDING + ' phase(s) pending.')
        }
    }
}

# ---- Default (advisory) path: byte-equivalent to v2.43 ----
if (-not $Gate) {
    Write-AdvisoryReport
    exit 0
}

# ---- Gate path (-Gate). Resolves to advisory unless every guard says block. ----

# Guard 1: gated mode. A .mode file must contain "gate".
#
# The project's root .mode is a FLOOR, not a default that slug scope replaces
# (issue #238). Reading only <plan-dir>\.mode let a slug plan with no .mode
# drop a project-committed gate. "gate" from EITHER file arms the gate; a slug
# may raise strictness, never lower it. In root scope $PlanDir already IS the
# project root, so the second source is skipped and behavior is unchanged.
$modeFile = Join-Path $PlanDir ".mode"
$rootForMode = if ($env:PWF_PLAN_ROOT) { $env:PWF_PLAN_ROOT } else { "." }
$rootModeFile = $null
if ($PlanDir -ne $rootForMode -and $PlanDir -ne ".") {
    $rootModeFile = Join-Path $rootForMode ".mode"
}
$gatedMode = $false
foreach ($candidateMode in @($modeFile, $rootModeFile)) {
    if (-not $candidateMode) { continue }
    if (-not (Test-Path $candidateMode)) { continue }
    $modeContent = Get-Content $candidateMode -Raw -ErrorAction SilentlyContinue
    if ($null -ne $modeContent -and $modeContent -match "gate") {
        $gatedMode = $true
        break
    }
}
if (-not $gatedMode) {
    Write-AdvisoryReport
    exit 0
}

# Guard 3: stop_hook_active. Read stdin only when input is redirected, so an
# interactive console never blocks. A true value means we are already inside a
# forced continuation; allow the stop.
$stdinJson = ""
try {
    if ([Console]::IsInputRedirected) {
        $stdinJson = [Console]::In.ReadToEnd()
    }
} catch {
    $stdinJson = ""
}
# Anchor on the literal value: "stop_hook_active" then colon then exactly true,
# with a JSON-structural boundary after it (whitespace, comma, closing brace, or
# end of input). Without the boundary 'true' could match a longer token; the
# boundary keeps a 'false' value (or any other key set to true) from tripping
# the guard and silently disabling the gate.
if ($stdinJson -match '"stop_hook_active"\s*:\s*true(\s|,|}|$)') {
    Write-AdvisoryReport
    exit 0
}

# Guard 2: an in_progress phase must exist.
if ($IN_PROGRESS -le 0) {
    Write-AdvisoryReport
    exit 0
}

# ledger_line_count: total lines across all <plan-dir>/ledger-*.jsonl files.
function Get-LedgerLineCount {
    $total = 0
    $files = Get-ChildItem -Path $PlanDir -Filter "ledger-*.jsonl" -File -ErrorAction SilentlyContinue
    foreach ($f in $files) {
        $lines = @(Get-Content $f.FullName -ErrorAction SilentlyContinue)
        $total                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          