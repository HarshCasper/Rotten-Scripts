package convert

import (
	"os/exec"
)

func ConvertFiles(path string, output string) error {

	ffmpeg := exec.Command("ffmpeg", "-i", path, "-r", "5", output)
	if err := ffmpeg.Run(); err != nil {
		return err
	}
	return nil
}
