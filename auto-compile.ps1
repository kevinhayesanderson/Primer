# auto-compile.ps1 main.py

param (
    [string]$file_name
)

while ($true) { 
    $before = Get-Item $file_name | Select-Object -ExpandProperty LastWriteTime
    Start-Sleep -Seconds 1
    $after = Get-Item $file_name | Select-Object -ExpandProperty LastWriteTime
    if ($before -ne $after) {
        python $file_name
    }
}