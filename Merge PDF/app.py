from os import listdir,mkdir,startfile,path
from os.path import isfile, join,exists
from PyPDF2 import PdfFileMerger

#Input file path and print the pdf files in that path
path = input("Enter the folder location: ")
pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]
print('\nList of PDF Files:\n')
for file in pdffiles:
    print(file)

#Input the name of the result file
resultFile = input("\nEnter the name of the result file : ")
if '.pdf' not in resultFile:
    resultFile += '.pdf' 

#Append the pdf files
merger = PdfFileMerger()
for pdf in pdffiles:
    merger.append(path+'\\'+pdf)

#If the Output directory does not exist then create one
if not exists(path+'\\Output'):
    mkdir(path+'\\Output')    

#Write the merged result file to the Output directory
merger.write(path+'\\Output\\'+resultFile)
merger.close()

#Launch the result file
print('\n'+resultFile,'Successfully created!!! at ',path+'\\Output\\')
startfile(path+'\\Output\\'+resultFile)