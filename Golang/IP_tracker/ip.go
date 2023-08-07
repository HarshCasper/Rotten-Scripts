//Looking up IP addresses for given host name//

package main

import (
	"fmt"
	"log"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatal("No valid hostname provided")
	}
	arg := os.Args[1]
	fmt.Println("Looking up IP addresses for given host name :" + arg)

	ip, err := net.LookupHost(arg)
	if err != nil {
		log.Fatal(err)
	}
	for _, ips := range ip {
		fmt.Println(ips)
	}
}
