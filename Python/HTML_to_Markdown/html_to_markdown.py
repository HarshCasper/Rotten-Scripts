import html2markdown
import sys

input_html = sys.argv[1]
output_md = sys.argv[2]

html_file = open(input_html, "r")

md_file = open(output_md, "w")

for data in html_file:

    md_file.write(html2markdown.convert(data))
    md_file.write("\n")
