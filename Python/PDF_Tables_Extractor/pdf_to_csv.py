""" python code to convert pdf to csv
"""
import sys
import tabula


def extract_tables(path, number_pages):
    tables = tabula.read_pdf(path, multiple_tables=True, pages=number_pages)
    num = 1
    if tables:
        for table in tables:
            print("Saving file ...")
            table.to_csv(f"Table-{num}.csv")
            num += 1
        print(f"created a csv file!'Table-{num}.csv'")
    else:
        print("No tables found !")


extract_tables(sys.argv[1], sys.argv[2])
