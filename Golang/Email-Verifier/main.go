package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
)

func main() {

	domain_sc := bufio.NewScanner(os.Stdin)
	fmt.Println("*-------------------*")
	fmt.Println("E-MAIL LOOKUP TOOL:")
	fmt.Println("*-------------------*")
	fmt.Printf("Enter domain:")

	for domain_sc.Scan() {
		checkDomain(domain_sc.Text())
	}

	if err := domain_sc.Err(); err != nil {
		log.Fatal("!!!Error in input!!! %v\n", err)
	}
}

func checkDomain(domain string) {

	var hasMX, hasSPF, hasDMARC bool
	var spfRecord, dmarcRecord, mxrecord string

	mxRecords, err := net.LookupMX(domain)

	if err != nil {
		log.Printf("!!!Error!!! %v\n", err)
	}

	if len(mxRecords) > 0 {
		hasMX = true
	}

	txtRecords, err := net.LookupTXT(domain)

	if err != nil {
		log.Printf("Error:%v\n", err)
	}

	for _, record := range txtRecords {
		if strings.HasPrefix(record, "v=spf1") {
			hasSPF = true
			spfRecord = record
			break
		}
	}

	mxrecords, _ := net.LookupMX(domain)
	for _, mx := range mxrecords {
		mxrecord = mx.Host
	}

	dmarcRecords, err := net.LookupTXT("_dmarc." + domain)
	if err != nil {
		log.Printf("ErrorL%v\n", err)
	}

	for _, record := range dmarcRecords {
		if strings.HasPrefix(record, "v=DMARC1") {
			hasDMARC = true
			dmarcRecord = record
			break
		}
	}
	fmt.Println("------------")
	fmt.Println("E-MAIL INFO:")
	fmt.Println("------------")
	fmt.Println(" ")

	fmt.Println("********BEGIN********")
	fmt.Println(" ")

	fmt.Printf("| Domain: %v | \n| MX_Status: %v | \n| MX_Record: %v | \n| SPF_Status: %v | \n|SPF Record: %v | \n|DMARC_Status: %v | \n|DMARC Record: %v |", domain, hasMX, mxrecord, hasSPF, spfRecord, hasDMARC, dmarcRecord)
	fmt.Println(" ")
	fmt.Println(" ")

	fmt.Println("*****END OF INFO*****")
	os.Exit(0)
}
