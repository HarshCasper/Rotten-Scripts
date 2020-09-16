import tabula


def extract_tables(path, number_pages):
    tables = tabula.read_pdf(path, multiple_tables=True, pages=number_pages)
    num = 1
    if len(tables) != 0:
        for table in tables:
            print("Saving file ...")
            table.to_csv(f'Table-{num}.csv')
            num += 1
        print("created a csv file!")
    else:
        print("No tables found !")


path = input("Enter the path to pdf file")
n = input("Enter number of pages to extract")
extract_tables(path, n)

