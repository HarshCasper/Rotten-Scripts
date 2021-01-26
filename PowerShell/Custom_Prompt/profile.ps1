# check if admin
function Test-Administrator {
    $user = [Security.Principal.WindowsIdentity]::GetCurrent();
    (New-Object Security.Principal.WindowsPrincipal $user).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

# custom prompt function
# Write-Host function is used to format print a string
# You may add more functions like conda or delete a function
function Prompt {

    Write-Host "[" -NoNewline -ForegroundColor DarkGray

    # current time
    Write-Host (Get-Date -format "HH:MM") -NoNewline -ForegroundColor Magenta
    Write-Host "]-[" -NoNewline -ForegroundColor DarkGray

    # Use different username if elevated
    if (Test-Administrator) {  
        Write-Host "Admin" -NoNewline -ForegroundColor Red
    } else {
        Write-Host "$ENV:USERNAME@$ENV:COMPUTERNAME" -NoNewline -ForegroundColor Cyan
    }
    Write-Host "]-[" -NoNewline -ForegroundColor DarkGray

    # current directory
    Write-Host (Get-Location) -NoNewline -ForegroundColor Blue

    Write-Host "] " -NoNewline -ForegroundColor DarkGray

    # git status
    $branch = git rev-parse --abbrev-ref HEAD

    if ($branch -ne $NULL) {
        # we're on an actual branch, so print it
        Write-Host "($branch)" -ForegroundColor Green
    } else {
        Write-Host ""
    }

    return "> "
}
