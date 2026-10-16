$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$transcribe = Join-Path $PSScriptRoot "transcribe.py"
$folders = @(
    (Join-Path $PSScriptRoot "ANN2DL"),
    (Join-Path $PSScriptRoot "Data Mining"),
    (Join-Path $PSScriptRoot "Multi agents"),
    (Join-Path $PSScriptRoot "SMBUD"),
    (Join-Path $PSScriptRoot "SOFTW2"),
    (Join-Path $PSScriptRoot "TCS")
)

if (-not (Test-Path -LiteralPath $python)) {
    throw "Virtual-environment Python was not found: $python"
}

foreach ($folder in $folders) {
    Write-Host "`nTranscribing: $folder" -ForegroundColor Cyan
    & $python $transcribe $folder --models parakeet
    if ($LASTEXITCODE -ne 0) {
        throw "Transcription failed for: $folder"
    }
}

# Successful transcripts no longer need their resumable chunk caches.
$repositoryRoot = [System.IO.Path]::GetFullPath($PSScriptRoot).TrimEnd('\')
$repositoryPrefix = $repositoryRoot + '\'
$cacheDirectories = @(Get-ChildItem -LiteralPath $repositoryRoot -Directory -Filter ".asr-cache" -Recurse -Force)

foreach ($cacheDirectory in $cacheDirectories) {
    $resolvedCache = [System.IO.Path]::GetFullPath($cacheDirectory.FullName).TrimEnd('\')
    if (-not $resolvedCache.StartsWith($repositoryPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to remove cache outside the repository: $resolvedCache"
    }

    Write-Host "Removing ASR cache: $resolvedCache" -ForegroundColor DarkGray
    Remove-Item -LiteralPath $resolvedCache -Recurse -Force
}
