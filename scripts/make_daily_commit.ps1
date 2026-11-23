param (
    [string]$Date = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss+05:30"),
    [string]$Message = "chore(analytics): daily project maintenance and continuous enhancement"
)
$env:GIT_AUTHOR_DATE = $Date
$env:GIT_COMMITTER_DATE = $Date
git add -A
git commit -m "$Message"
git push origin main
Write-Host "Pushed daily commit for $Date with message: $Message"