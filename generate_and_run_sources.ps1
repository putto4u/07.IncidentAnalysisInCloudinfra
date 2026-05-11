$ErrorActionPreference = "Continue"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$targetMin = 61
$targetMax = 75
$sourceSuffix = "(" + [char]0xC18C + [char]0xC2A4 + ").py"

function Get-ChecklistByTopic {
    param([string]$baseName)
    $name = $baseName.ToLowerInvariant()

    if ($name -match "downloader|download") { return @("Check URL allowlist", "Verify file hash", "Block post-download execution") }
    if ($name -match "dropper") { return @("Monitor dropped file path", "Check dropped extension", "Inspect autorun traces") }
    if ($name -match "c2|network|beacon") { return @("Identify beacon interval", "Check destination reputation", "Detect anomalous user-agent") }
    if ($name -match "privilege|elevation") { return @("Review privilege change logs", "Inspect UAC bypass traces", "Track admin session abuse") }
    if ($name -match "ransom") { return @("Detect mass file rewrite", "Watch extension rename spikes", "Alert on backup delete commands") }
    if ($name -match "keylog") { return @("Inspect keyboard hook calls", "Analyze clipboard access rate", "Detect hidden log artifacts") }
    if ($name -match "exfil|steal") { return @("Detect unusual upload traffic", "Check compressed outbound payloads", "Monitor off-hours bulk transfer") }
    if ($name -match "obfus|deobfus") { return @("Find encoded string patterns", "Separate decode routines", "Peel obfuscation layers") }
    if ($name -match "vba|macro") { return @("Inspect AutoOpen routines", "Check Shell and WinAPI calls", "Correlate document-process chain") }
    if ($name -match "powershell|amsi|wmi") { return @("Detect EncodedCommand usage", "Review ScriptBlock logs", "Flag AMSI bypass patterns") }
    if ($name -match "pdf|hwp|dde|document") { return @("Inspect embedded script objects", "Check external object references", "Review viewer trigger patterns") }
    if ($name -match "ddos") { return @("Detect traffic surge", "Check distributed C2 pattern", "Inspect reflection-amplification traces") }
    return @("Review network indicators", "Review file activities", "Review process lineage")
}

function Escape-SingleQuote {
    param([string]$text)
    return $text -replace "'", "''"
}

$dirs = Get-ChildItem -LiteralPath $root -Directory | Where-Object {
    $_.Name.Length -ge 3 -and
    $_.Name.Substring(0,3) -match '^\d{3}$' -and
    [int]$_.Name.Substring(0,3) -ge $targetMin -and
    [int]$_.Name.Substring(0,3) -le $targetMax
} | Sort-Object Name

$created = 0

foreach ($dir in $dirs) {
    $mdFiles = Get-ChildItem -LiteralPath $dir.FullName -File -Filter "*.md" | Sort-Object Name

    foreach ($md in $mdFiles) {
        $base = [System.IO.Path]::GetFileNameWithoutExtension($md.Name)
        $pyPath = Join-Path $md.DirectoryName ($base + $sourceSuffix)
        $topic = Escape-SingleQuote $base
        $list = Get-ChecklistByTopic -baseName $base

        $content = @"
# This file is a harmless lab source mapped to '$base'.
"""Defensive training source for: $base."""

# Import json for formatted output.
import json
# Import platform to capture runtime OS.
import platform
# Import datetime for UTC timestamp.
from datetime import datetime, timezone

# Fix the topic using the lesson file name.
TOPIC = '$topic'
# Mark this source as defensive only.
MODE = 'defensive-training'

# Build metadata for this run.
def build_metadata() -> dict:
    # Create ISO timestamp in UTC.
    now = datetime.now(timezone.utc).isoformat()
    # Collect current OS name.
    os_name = platform.system()
    # Return metadata dictionary.
    return {
        'topic': TOPIC,
        'mode': MODE,
        'timestamp': now,
        'os': os_name,
        'safety': 'no offensive behavior',
    }

# Build topic-aware checklist items.
def build_checklist() -> list[str]:
    # Define first checklist item.
    item1 = '$($list[0])'
    # Define second checklist item.
    item2 = '$($list[1])'
    # Define third checklist item.
    item3 = '$($list[2])'
    # Return checklist list.
    return [item1, item2, item3]

# Build final result object.
def build_result() -> dict:
    # Create metadata.
    metadata = build_metadata()
    # Create checklist.
    checklist = build_checklist()
    # Return combined result.
    return {'metadata': metadata, 'checklist': checklist}

# Main execution function.
def main() -> None:
    # Build final result.
    result = build_result()
    # Print as pretty JSON.
    print(json.dumps(result, ensure_ascii=False, indent=2))

# Run main only when executed directly.
if __name__ == '__main__':
    # Execute main.
    main()
"@

        Set-Content -LiteralPath $pyPath -Value $content -Encoding UTF8
        $created += 1
    }
}

$pythonCmd = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py -3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
}

$logDir = Join-Path $root "_run_logs"
New-Item -ItemType Directory -Path $logDir -Force | Out-Null
$summaryPath = Join-Path $logDir "run_summary.txt"
"created_sources=$created" | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if (-not $pythonCmd) {
    Add-Content -LiteralPath $summaryPath -Value "python_runtime=missing"
    Add-Content -LiteralPath $summaryPath -Value "run_status=skipped"
    Write-Output "Done: sources created. Python runtime is missing, run skipped."
    exit 0
}

$sourceFiles = Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object {
    $_.Name.EndsWith($sourceSuffix) -and
    $_.Directory.Name.Length -ge 3 -and
    $_.Directory.Name.Substring(0,3) -match '^\d{3}$' -and
    [int]$_.Directory.Name.Substring(0,3) -ge $targetMin -and
    [int]$_.Directory.Name.Substring(0,3) -le $targetMax
} | Sort-Object FullName

$ok = 0
$fail = 0

foreach ($src in $sourceFiles) {
    $logName = ($src.BaseName + ".log")
    $logPath = Join-Path $logDir $logName
    $cmd = "$pythonCmd `"$($src.FullName)`""
    Invoke-Expression $cmd 2>&1 | Set-Content -LiteralPath $logPath -Encoding UTF8
    if ($LASTEXITCODE -eq 0) {
        $ok += 1
        Add-Content -LiteralPath $summaryPath -Value ("OK`t" + $src.FullName)
    } else {
        $fail += 1
        Add-Content -LiteralPath $summaryPath -Value ("FAIL`t" + $src.FullName)
    }
}

Add-Content -LiteralPath $summaryPath -Value ("run_ok=" + $ok)
Add-Content -LiteralPath $summaryPath -Value ("run_fail=" + $fail)
Write-Output ("Done: created " + $created + ", run ok " + $ok + ", run fail " + $fail)
