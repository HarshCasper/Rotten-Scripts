from pdfrw import PdfReader, PdfWriter
"""
The function input_and_parse gathers the inputs and parses and then sorts them in
the order required by reorder(path,dic) function
It takes one argument which is page length of pdf 'n'
"""


def input_and_parse(n):
    print("enter the current page and the page you want it to be on seperate values by a comma ',' \n")
    """
    store the input in a list and then convert the input string into
    using map function to convert the data in lists into int values
    """
    lst = list(map(lambda x: [int(x[0]), int(x[1])],
                   [input().split(',') for _ in range(n)]))
    # Swapping the position of the lst values to better parse it in dictionary
    lst = [[x[1], x[0]] for x in lst]
    lst.sort(key=lambda x: x[0])
    dic = {curr: new for curr, new in lst}
    # now I have sorted the dic to the required needs of reorder function
    return dic


"""
The function reorder takes two arguments path and dic
path is the path of the source pdf file which is in wrong
order
"""


def reorder(path, dic):
    # create a pdf object using PdfReader that could be read
    pdf_obj = PdfReader(path)
    # pdf_obj.pages attribute gives the length of the pages in pdf
    total_pages = len(pdf_obj.pages)
    print("Total Pages in PDF are:", total_pages)
    # Initialising the writer object using the PdfWriter class,from this we would create a new modified Pdf
    writer = PdfWriter()

    # new and old here mean the new position of the "old" page location
    for new, old in dic.items():
        # indexing pages list
        writer.addpage(pdf_obj.pages[old-1])
        print(f"page{new} added from {old}")

    # accesing the name of the file without .pdf to save it with a new one
    writer.write(path[:-4]+"-modified.pdf")


if __name__ == "__main__":
    path = input("Enter the path of the pdf file:")
    dic = input_and_parse(len(PdfReader(path).pages))
    reorder(path, dic)
    print("New modified pdf file created succesfully!")
