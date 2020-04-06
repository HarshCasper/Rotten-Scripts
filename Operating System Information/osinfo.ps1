#.ps1   
    $wmiobject =  get-wmiobject -class win32_operatingsystem
    $user = ($wmiobject).RegisteredUser
    $kernal_version = ($wmiobject).Version
    Write-host -fore green "The victim is running on kernal $kernal_version ","With the username $user & Computername is $(whoami) ."
