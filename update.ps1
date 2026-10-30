param(
    [switch]$NoPush,
    [switch]$AwesomeOnly,
    [switch]$About,
    [switch]$Tags,
    [switch]$Reindex,
    [switch]$Push,
    [string]$Tag = "",
    [string]$Find = ""
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$argsList = @()
if ($NoPush) { $argsList += "--no-push" }
if ($AwesomeOnly) { $argsList += "--awesome" }
if ($About) { $argsList += "--about" }
if ($Tags) { $argsList += "--tags" }
if ($Reindex) { $argsList += "--reindex" }
if ($Push) { $argsList += "--push" }
if ($Tag -ne "") { $argsList += @("--tag", $Tag) }
if ($Find -ne "") { $argsList += @("--find", $Find) }

python "$scriptDir\update.py" @argsList
