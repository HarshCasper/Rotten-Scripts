import json
import xlwt
import sys
import os

if sys.argv[1] == "help":
    print("Usage:\n\tjsonToExcel.py json_file.json")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("Cannot open " + sys.argv[1])
    sys.exit(1)

file_name = sys.argv[1]
extension = file_name.split(".")[-1]

if not extension in ("json"):
    print("The extension of json_file is incorrect")
    sys.exit(1)

file = open(file_name)
text_json = file.read()

try:
    json_imported = json.loads(text_json)
except:
    print("The content of json_file is incorrect")
    sys.exit(1)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("json exported")

columns = list(json_imported[0].keys())

i = 0
for column in columns:
    worksheet.write(0, i, column)
    i += 1

j = 1
for row in json_imported:
    i = 0
    for column in columns:
        worksheet.write(j, i, row[column])
        i += 1
    j += 1

try:
    workbook.save(file_name.split(".")[0] + ".xls")
    sys.exit(0)
except:
    print("Can't write the xls file")
    sys.exit(1)
