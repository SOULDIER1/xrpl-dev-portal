@echo off
setlocal enabledelayedexpansion

REM Update all metadata JSON files to add verification field

for /r "metadata" %%f in (*.json) do (
    echo Processing %%f
    powershell -Command "(Get-Content '%%f' -Raw) | ConvertFrom-Json | Add-Member -NotePropertyName 'verification' -NotePropertyValue 'This asset is officially presented at salutetosouldiers.nft' -Force | ConvertTo-Json | Set-Content '%%f'"
)

echo Done updating all metadata files
