package main

import (
	"flag"
	"fmt"
	"gif/convert"
	"image"
	"image/color/palette"
	"image/draw"
	"image/gif"
	_ "image/jpeg"
	"io/ioutil"
	"os"
)

var option, output, input string
var delay int

func main() {

	flag.StringVar(&option, "s", "", "s=image for image to GIF and s=video for video to GIT")
	flag.StringVar(&input, "i", "", "path to the folder containing images")
	flag.StringVar(&output, "o", "output.gif", "the name of the generated GIF")
	flag.Parse()

	if input == "" {
		fmt.Println("A path is required")
		flag.PrintDefaults()
		return
	}
	if output == "" {
		output = "genrated.gif"
		flag.PrintDefaults()
		return
	}
	if option == "" {
		fmt.Println("Enter image if you want to convert image to gif or else enter video")
		flag.PrintDefaults()
		return
	}
	if option == "image" {
		imagetoGIF(input, output)
	} else if option == "video" {
		videoToGIF(input, output)
	}

}

func videoToGIF(path string, output string) {

	err := convert.ConvertFiles(path, output)
	if err != nil {
		fmt.Println(err)
		fmt.Println("error in converting")
	}
}
func imagetoGIF(path string, output string) {

	delay := 3
	files, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println(err)
		return
	}

	anim := gif.GIF{}
	for _, info := range files {
		f, err := os.Open(path + "/" + info.Name())
		if err != nil {
			fmt.Printf("Could not open file %s. Error: %s\n", info.Name(), err)
			return
		}
		defer f.Close()
		img, _, _ := image.Decode(f)

		// Image has to be palleted before going into the GIF
		paletted := image.NewPaletted(img.Bounds(), palette.Plan9)
		draw.FloydSteinberg.Draw(paletted, img.Bounds(), img, image.ZP)

		anim.Image = append(anim.Image, paletted)
		anim.Delay = append(anim.Delay, delay*100)
	}

	f, _ := os.Create(output)
	defer f.Close()
	gif.EncodeAll(f, &anim)
}
