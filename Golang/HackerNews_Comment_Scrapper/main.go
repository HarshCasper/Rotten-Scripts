package main

import (
	"encoding/json"
	"fmt"
	"strings"
	"io/ioutil"
    "log"
	"github.com/gocolly/colly"
)

type Comment struct{
	Comment_text string 
}
func main(){
	comments := make([]Comment,0)

	// Instantiate default collector
	c := colly.NewCollector()

	c.OnHTML(".comment-tree .comment", func(element *colly.HTMLElement){
	comm:=strings.TrimSpace(element.Text)

	comment:= Comment{
		Comment_text: comm,
	}

	comments = append(comments,comment)
})

c.OnRequest(func(request *colly.Request) {
	fmt.Println("Visiting", request.URL.String())
})

c.Visit("https://news.ycombinator.com/item?id=27750040") // Change URL here

writeJSON(comments)

}

func writeJSON(data []Comment) {
    file, err := json.MarshalIndent(data, "", " ")
    if err != nil {
        log.Println("Unable to create json file")
        return
    }

    _ = ioutil.WriteFile("output.json", file, 0644)
	fmt.Println("output.json Added")
}