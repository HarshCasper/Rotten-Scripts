file_path = input("Enter the tsv file path : ")

tsv_file = open(file_path, 'r')

tsv_content = tsv_file.read()

csv_content = tsv_content.replace("\t", ",")

csv_file = open('converted-csv.csv', 'w')

csv_file.write(csv_content)
csv_file.close()
print("Task Comeplted, TSV Converted to CSV") 