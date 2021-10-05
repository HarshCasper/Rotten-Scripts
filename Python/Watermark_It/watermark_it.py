import pdfrw
import sys
import os

# Function for taking pdf inputs and validating them


def input_and_validate():
    # The pdf file which you want to watermark
    file_to_be_watermarked = input("Enter the file you want to watermark: ")

    # To ensure that the user inputs only pdf files
    if file_to_be_watermarked.endswith(".pdf") is False:
        sys.exit("Please enter only pdf files")

    # To check if the file to be watermarked is present in the current directory or not
    if os.path.exists(file_to_be_watermarked) is False:
        sys.exit(file_to_be_watermarked + " is not present in the directory")

    # The pdf file which contains the watermark
    file_containing_watermark = input("Enter the file which has the watermark: ")

    # To ensure that the user inputs only pdf files
    if file_containing_watermark.endswith(".pdf") is False:
        sys.exit("Please enter only pdf files")

    # To check if the file containing the  watermark is present in the current directory or not
    if os.path.exists(file_containing_watermark) is False:
        sys.exit(file_containing_watermark + " is not present in the directory")

    return [file_to_be_watermarked, file_containing_watermark]


# Function to read the pdfs and watermark the base pdf


def watermark_it(file_to_be_watermarked, file_containing_watermark):
    # Reading the file which has to be watermarked and storing it as an object
    base_file_object = pdfrw.PdfReader(file_to_be_watermarked)

    # Initialising a writer object
    writer_object = pdfrw.PdfWriter()

    # Reading the file which contains the watermark and storing it as an object
    watermark_object = pdfrw.PdfReader(file_containing_watermark)

    # Extracting the watermark from the watermark object
    watermark = watermark_object.pages[0]

    total_pages_in_base_file = len(base_file_object.pages)

    # Main logic to add watermark to all pages of the pdf
    for page in range(total_pages_in_base_file):

        # Creating a merge object for all the pages of the pdf
        merge_object = pdfrw.PageMerge(base_file_object.pages[page])

        # Adding the watermark to all the pages through the merge object
        merge_object.add(watermark).render()

    # Creating an output file with modified name
    watermarked_output = (
        "watermarked_" + file_to_be_watermarked.split(".pdf")[0] + ".pdf"
    )

    # Writing the merged base file object to the output file
    writer_object.write(watermarked_output, base_file_object)

    print("Your pdf file has been successfully watermarked!!!!")


def main():

    base_pdf, watermark_pdf = input_and_validate()
    watermark_it(base_pdf, watermark_pdf)


main()
