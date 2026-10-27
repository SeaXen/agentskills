param(
    [switch]$NoPush,
    [switch]$AwesomeOnly,
    [switch]$About,
    [switch]$Tags,
    [string]$Tag = ""
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$argsList = @()
if ($NoPush) { $argsList += "--no-push" }
if ($AwesomeOnly) { $argsList += "--awesome" }
if ($About) { $argsList += "--about" }
if ($Tags) { $argsList += "--tags" }
if ($Tag -ne "") { $argsList += @("--tag", $Tag) }

python "$scriptDir\update.py" @argsList
