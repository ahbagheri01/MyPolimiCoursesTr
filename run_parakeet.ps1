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
