package main

import (
	"fmt"

	"github.com/gocolly/colly"
)

func main() {
	give_current_price_of_bitcoin()
}

func give_current_price_of_bitcoin() {
	c := colly.NewCollector(
		colly.AllowedDomains("google.com", "www.google.com"),
	)

	found := false //bool variable to close the search after target tag is found

	c.OnHTML("div", func(e *colly.HTMLElement) {

		if found {
			return //return nothing when target tag is matched
		}

		if e.Attr("class") == "BNeawe iBp4i AP7Wnd" {
			fmt.Printf("1 BTC = %s\n", e.Text)
			found = true
		}
	})
	c.Visit("https://www.google.com/search?q=bitcoin+price") //webpage url to be visited
}
