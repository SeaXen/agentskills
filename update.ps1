param(
    [switch]$NoPush,
    [switch]$AwesomeOnly
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$argsList = @()
if ($NoPush) { $argsList += "--no-push" }
if ($AwesomeOnly) { $argsList += "--awesome" }

python "$scriptDir\update.py" @argsList
