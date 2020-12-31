from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()
 
# I had 2 files in the folder that had to be merged into a single document
for fileNumber in range(1,3): #change value in range according to files+1 you have.
    mergedObject.append(PdfFileReader('Sample_Pdf' + str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("Merged_File.pdf")