
## This script can pe used for testing the script pdf_reorder.py
## with a random pdf with pages in wrong order 
## I have written this script so that
## the pages on generated pdf will have a page with numbers
## ofcourse in wrong order ;)

#shuffle is used to shuffle a list
from random import shuffle 
from fpdf import FPDF

# save FPDF() class into a 
# variable pdf 
pdf = FPDF()

no_of_pages=int(input("Enter the no. of pages for new .pdf file:"))

right_numbers=list(range(1,no_of_pages+1))
temp=right_numbers[:]
shuffle(temp)
wrong_numbers=temp[:]
del temp

for num in range(no_of_pages):
    pdf.add_page()
    pdf.set_font("Arial", size =30)
    pdf.cell(200, 10, txt = "Page with number"+str(wrong_numbers[num]),ln = 1, align = 'C') 

pdf.output("wrong.pdf") 

print("pdf file created with pages in wrong order")
pairs=zip(right_numbers,wrong_numbers)
print("\n"*2)
print("pairs of pages with right,wrong format you can use this in pdf_reorder.py script")

for right,wrong in pairs:
    print(f"{right},{wrong}")

    
