from PyPDF2 import PdfFileReader, PdfFileWriter, utils


def is_encrypted(filename: str) -> bool:
    with open(filename, 'rb') as f:
        pdf_reader = PdfFileReader(f, strict=False)
        return pdf_reader.isEncrypted


def encrypt_file(filename: str, password: str) -> str:
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(filename, 'rb'), strict=False)
    if is_encrypted(filename):
        return "PDF File is already encrypted."

    try:
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError:
        return "Error while reading PDF file"

    pdf_writer.encrypt(user_pwd=password, use_128bit=True)
    with open("encrypted_demo.pdf", "wb") as f:
        pdf_writer.write(f)

    return "PDF file encrypted successfully"


def decrypt_file(filename: str, password: str) -> str:
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(filename, 'rb'), strict=False)
    if not is_encrypted(filename):
        return "PDF File is not encrypted."

    pdf_reader.decrypt(password=password)
    try:
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError:
        return "Error while reading PDF file"

    with open("decrypted_demo.pdf", "wb") as f:
        pdf_writer.write(f)

    return "PDF file decrypted successfully"


print(encrypt_file('demo.pdf', 'iRead'))
print(decrypt_file('encypted_demo.pdf', 'iRead'))
