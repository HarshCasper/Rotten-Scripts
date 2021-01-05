from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdf(files, output):
    pdf_writer = PdfFileWriter()

    for f in files:
        pdf_reader = PdfFileReader(f)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


#driver code
if __name__ == '__main__':
    paths = ['Logic_and_Discrete_Mathematics_-_Willem.pdf', 'Deep Learning with Keras_ Implementing deep learning models and neural networks with the power of Python.pdf']
    merge_pdf(paths, output='merged.pdf')
