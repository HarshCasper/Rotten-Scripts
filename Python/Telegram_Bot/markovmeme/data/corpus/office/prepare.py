#!/usr/bin/env python3

import re
import json

with open("office_transcript.csv", "r") as filey:
    content = filey.readlines()

lines = {}

for row in content:
    for line in row.split(","):
        line = " ".join(line.split(";")[1:]).strip()
        if line and ":" in line:
            char, rest = line.split(":", 1)
            line = "".join(rest)
            if char not in lines:
                lines[char] = []
            # Clean up the line
            line = line.replace("'", "").replace('"', "").replace("\n", "").strip()
            line = re.sub("\[.*?\]", " ", line).replace("[", " ").replace("]", "")
            lines[char].append(line.strip())

# Keep an organized json for later...
with open("office.json", "w") as filey:
    filey.writelines(json.dumps(lines, indent=4))

# Dump office lines into files, for all office or individual characters
with open("../the_office.txt", "w") as filey:
    for char, sentences in lines.items():
        for sentence in sentences:
            filey.write("%s\n" % sentence)


# Print lines for all characters > 100
for char, sentences in lines.items():
    if len(sentences) > 100:
        with open("%s.txt" % char.lower(), "w") as filey:
            for sentence in sentences:
                filey.write("%s\n" % sentence)
