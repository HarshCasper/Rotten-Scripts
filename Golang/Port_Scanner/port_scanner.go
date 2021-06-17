package main

import (
	"fmt"
	"net"
	"strings"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {

	var option int
	var ip string
	fmt.Print("[+] Enter IP address to scan: ")
	fmt.Scan(&ip)

	var typeOfPort string
	fmt.Print("[+] Enter type of port you want to scan for eg(tcp,udp..etc): ")
	fmt.Scan(&typeOfPort)

	fmt.Print("[+] For scanning all open ports press : 1 \n[+]For scanning Specific ports press :2 \n")
	fmt.Scan(&option)
	if option == 1 {
		scanAllPorts(ip, typeOfPort)
	} else if option == 2 {
		scanSelectedPorts(ip, typeOfPort)
	} else {
		fmt.Println("Please chose valid option")
	}
}

// function for scanning all Ports
func scanAllPorts(ip string, typeOfPort string) {
	wg.Add(65535)
	for port := 1; port <= 65535; port++ {
		go func(port int) {
			defer wg.Done()
			hostIp := fmt.Sprintf("%s:%d", ip, port)
			// fmt.Println(hostIp)

			_, err := net.DialTimeout(typeOfPort, hostIp, 10*time.Millisecond)

			if err == nil {
				fmt.Printf("Port %d is open \n", port)
			}
		}(port)
	}
	wg.Wait()
}

// function for scanning specific Ports
func scanSelectedPorts(ip string, typeOfPort string) {
	var portsInput string
	fmt.Print("[+] Enter Ports to scan: ")
	fmt.Scan(&portsInput)
	ports := strings.Split(portsInput, ",")
	for _, port := range ports {
		hostIp := fmt.Sprintf("%s:%s", ip, port)

		_, err := net.DialTimeout(typeOfPort, hostIp, 80*time.Millisecond)
		if err != nil {
			fmt.Printf("Port %s is closed \n", port)
		} else {
			fmt.Printf("Port %s is open \n", port)
		}
	}
}
