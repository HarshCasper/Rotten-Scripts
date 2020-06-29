package main

import (
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/badoux/goscraper"
)

func main() {
	fmt.Println("Welcome to Github_UserName_Checker\n Rules:\n1.Github username may only contain alphanumeric characters or hyphens.\n2.Github username cannot have multiple consecutive hyphens.\n3.Github username cannot begin or end with a hyphen.\n4.Maximum is 39 characters.")
	getInput()
}

func getInput() {
	fmt.Println("\n\nEnter the Initial_Name: ")
	var initialName string

	_, err := fmt.Scanln(&initialName)
	if err != nil {
		log.Fatal("error occured while taking input : ", err)
	}

	length := len(initialName)

	switch checkerror(initialName, length) {
	case 1:
		fmt.Println("Read the Rules carefully:\nUsername must only alphanumeric character")
		getInput()
	case 2:
		fmt.Println("Read the Rules carefully:\nHyphens not allowed at begining")
		getInput()
	case 3:
		fmt.Println("Read the Rules carefully:\nHyphens not allowed at end")
		getInput()
	case 4:
		fmt.Println("Read the Rules carefully:\nLength should not be  greater than 39 characters")
		getInput()
	case 5:
		fmt.Println("Read the Rules carefully:\nConsecutive hyphen not allowed")
		getInput()
	case 6:
		checkUserName(initialName)
	}

}

func checkerror(initialName string, length int) int {
	if notAlphaNumeric(initialName, length) {
		return 1
	}
	if initialName[0] == '-' {
		return 2
	}
	if length == 39 && initialName[length-1] == '-' {
		return 3
	}
	if length > 39 {
		return 4
	}
	if doubleHyphen(initialName, length) {
		return 5
	}
	return 6
}
func checkUserName(username string) {
	finalusername := username
	counter := 0
	for i := 48; i <= 57; i++ {
		if ping(finalusername) {
			counter++
			fmt.Printf("%v. %v\n", counter, finalusername)
		}
		finalusername = username + string(i)
	}
	for i := 65; i <= 90; i++ {
		finalusername = username + string(i)
		if ping(finalusername) {
			counter++
			fmt.Printf("%v. %v\n", counter, finalusername)
		}
	}
	csvFileName := flag.String("csv", "postfix.csv", "csv file in the formate of questions and answer")
	flag.Parse()
	file, err := os.Open(*csvFileName)
	if err != nil {
		log.Fatalln("Opening file failed: ", err)
	}

	r := csv.NewReader(file)
	lines, err := r.ReadAll()
	if err != nil {
		log.Fatalln("file parsing failed: ", err)
	}

	for _, line := range lines {
		finalusername = username + line[0]
		if ping(finalusername) {
			counter++
			fmt.Printf("%v. %v\n", counter, finalusername)
		}
	}

	if counter == 0 {
		fmt.Println("No Id with initial_name found")
	}

}

func ping(finalusername string) bool {
	finalurl := "https://github.com/" + finalusername

	s, err := goscraper.Scrape(finalurl, 10)
	if err != nil {
		fmt.Println("Scrapping failed : ", err)
	}
	//fmt.Printf("Title : %s\n", s.Preview.Title)
	if s.Preview.Title == "Build software better, together" {
		return true
	}
	return false
}

func notAlphaNumeric(username string, length int) bool {
	for i := 0; i < length; i++ {
		switch int(username[i]) {
		case 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122:
		default:
			return true
		}
	}
	return false
}

func doubleHyphen(name string, length int) bool {
	for i := 0; i < length-1; i++ {
		if name[i] == '-' && name[i+1] == '-' {
			return true
		}
	}
	return false

}
