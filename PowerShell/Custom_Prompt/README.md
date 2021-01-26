# Custom PowerShell Command Prompt

You can customise your PowerShell prompt to show more informations like git branch status, command execution time, current directory, admin status etc. *(This script is just an introduction how you can customise your PowerShell prompt, you can add several more customizations).* To read more about PowerShell Prompt go [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_prompts?view=powershell-7.1).

## Dependencies 

Git must be installed in order to utilise full potential of the script. Or you can safely comment the git code in the script. To install Git on Windows go [here](https://git-scm.com/download/win).

## Setup Instructions

1. Open a PowerShell prompt with admin. You can use `WinKey + X` to launch quick tools menu and select **Windows PowerShell (Admin)** 

2. Set script execution policy 

```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
```

3. Check if there is an existing configuration, if not create a new file.

```powershell
    if (!(Test-Path -Path $PROFILE)){ New-Item -Path $PROFILE -ItemType File } ; notepad $PROFILE
```

4. A file will open, if there is an exisiting `prompt` function in the file then change the contents else paste everything from [profile.ps1](profile.ps1) in the file.

5. Save and exit Notepad and relaunch PowerShell. 

## Output
- Simple mode

<a href="https://imgur.com/W9kOmLA"><img src="https://i.imgur.com/W9kOmLA.png" title="source: imgur.com" align=center /></a>

- Admin Mode

<a href="https://imgur.com/XBMLkJM"><img src="https://i.imgur.com/XBMLkJM.png" title="source: imgur.com" align=center /></a>

## Author(s)

Created by [Avinal Kumar](https://github.com/avinal)

