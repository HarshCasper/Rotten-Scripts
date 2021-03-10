import PyPDF2
import sys

# Open the pdf file
file1 = sys.argv[1]
file2 = sys.argv[2]
pdf1 = open(file1, 'rb')
pdf2 = open(file2, 'rb')

# Read the files
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)

# Create a new PdfFileWriter object which represents a blank PDF document
writer = PyPDF2.PdfFileWriter()

# Loop through all the pagenumbers for the first document
for i in range(reader1.numPages):
    pages = reader1.getPage(i)
    writer.addPage(pages)

# Loop through all the pagenumbers for the second document
for i in range(reader2.numPages):
    pages = reader2.getPage(i)
    writer.addPage(pages)

# Now that you have copied all the pages in both the documents, write them into the a new document
mergedfile = open('MergedFiles.pdf', 'wb')
writer.write(mergedfile)

# Close all the files - Created as well as opened
mergedfile.close()
pdf1.close()
pdf2.close()
