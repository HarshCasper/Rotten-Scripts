import sys
import os
import comtypes.client

pptxFormatPDF = 32

in_file = os.path.abspath(sys.argv[1])
out_file = os.path.abspath(sys.argv[2])

powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
powerpoint.Visible = 1
pptxx = powerpoint.Presentations.Open(in_file)
pptxx.SaveAs(out_file, pptxFormatPDF)
pptxx.Close()
powerpoint.Quit()

