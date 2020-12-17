
from pdfrw import PdfReader, PdfWriter

# The function input_and_parse gathers the inputs and parses and then sorts them in
# the order required by reorder(path,dic) function
#It takes one argument which is page length of pdf 'n'
 
def input_and_parse(n):
    print("="*20)
    print("enter the current page and the page you want it to be on seperate values by a comma ',' \n") 
    lst=[input().split(',') for _ in range(n)]
    dic={int(curr):int(new) for curr,new in lst}
    ## now I sort it to the required needs of reorder function
    lst=list(zip(dic.values(),dic.keys()))
    lst.sort(key=lambda x:x[0])
    dic=dict(lst)
    return dic
 
 
#The function reorder takes two arguments path and dic
#path is the path of the source pdf file which is in wrong
#order

def reorder(path,dic):
    pdf_obj = PdfReader(path)
    total_pages = len(pdf_obj.pages)
    writer = PdfWriter()
    for new,old in dic.items():
        writer.addpage(pdf_obj.pages[old-1])
        print(f"page{new} added from {old}")
    writer.write(path[:-4]+"-modified.pdf")

if __name__=="__main__":
    path=input("Enter the path of the pdf file:")
    dic=input_and_parse(len(PdfReader(path).pages))
    #print(dic)
    reorder(path,dic)
    print("New modified pdf file created succesfully!")
