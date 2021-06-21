from PyPDF2 import PdfFileReader, PdfFileWriter


def ifexists(total_pages, page_no):
    """
    This function checks whether the given page number is in the specified range
    of total pages.

    :param total_pages:
    :param page_no:
    :return: True or False
    """
    if page_no <= total_pages:
        return False
    return True


def reodering(path):
    """
    This function takes file location and then reorders it as specified by the user.
    and saves it into a pdf file with specified name into the current directory.
    :param path: File on which operation is going to perform
    """

    # Creating object of Read and Write functions of the Library.
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)

    # get total no.of pages ie length of PDF
    total_pages = pdf_reader.getNumPages()
    # creates a list of of total pages in ascending order
    ordered_pages = [i + 1 for i in range(total_pages)]

    # Taking input that how many pages want to reorder
    n = int(input("Enter the Total Number of pages which you want to reorder:"))

    # Taking user INPUT of page no and location you want to move that page
    print(
        "\nNow enter the Page no which you want to reorder with the expected location"
    )

    # Running a loop to take input
    for i in range(n):
        ans_1 = True
        while ans_1:
            page_no = int(input("Enter the Page No. you want to reorder: "))
            ans_1 = ifexists(total_pages, page_no)
            if ans_1:  # if the no. is invalid
                print("Invalid Page No. ")
                print(f"Enter a number below {total_pages}")

        ans_2 = True
        while ans_2:
            expected_location = int(input("Enter the location you want to reorder: "))
            ans_2 = ifexists(total_pages, expected_location)
            if ans_2:  # if location is in invalid
                print("Invalid Page No. ")
                print(f"Enter a number below {total_pages}")

        # removing the pages from the initial list so that we can
        # move it to the specified location
        ordered_pages.remove(page_no)
        # inserting the page no at the specified location
        ordered_pages.insert(expected_location - 1, page_no)

        print("Pages are going to be in these order: ", end="")
        print(ordered_pages, "\n")

    # if ordered pages are ready in a list then passing it further into write function
    print("\nPDF being prepared !")
    for page in ordered_pages:
        # adding pages in write function page by page
        pdf_writer.addPage(pdf_reader.getPage(page - 1))

    # Saving the PDF with the specified name
    output_file = (
        input("Enter the filename in which you want to save (without .pdf extension): ")
        + ".pdf"
    )
    with open(output_file, "wb") as fh:
        pdf_writer.write(fh)

    print(f"Great Success!!! Check your directory for {output_file} file!")


if __name__ == "__main__":
    path = input("Enter File name: ")
    reodering(path)
