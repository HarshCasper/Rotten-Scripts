
#.ps1
$ipadd = $args[0]
$port =  $args[1]
$scan =  test-netconnection -computername $ipadd -port $port -InformationLevel "Detailed"
        $tcp = ($scan).TcpTestSucceeded
        if ($tcp -eq "True")
        {
            Write-Host -fore green "Port $port is open!"
        }
        else {
            Write-Host -fore green "Port $port is closed!"
        }
