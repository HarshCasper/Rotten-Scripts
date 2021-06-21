import os
import csv


# The function that can be used to split a CSV file based on User Input
def split_rows(filename, delimiter=",", row_limit=1000, output_path="."):
    """
    CSV splitter using csv-python library.

    Arguments:
        `filename`:  The Input File Path
        `row_limit`: The number of rows every file should have, 1000 by default.
        `output_path`: Destination path. "pwd" by default.
    """
    # The Output name pattern
    output_name = "_Split(%s).csv"
    # Final Output File Names
    output_name_template = filename + output_name
    # File handler to open Input Files in Read Mode
    filehandler = open(filename + ".csv", "r")
    keep_headers = True
    input_file = csv.reader(filehandler, delimiter=delimiter)
    # Initialise the First Row
    current_row = 1
    # Initialise the Output path
    current_out_path = os.path.join(output_path, output_name_template % current_row)
    # File handler to write into the Initialised CSV file
    writer = csv.writer(open(current_out_path, "w"), delimiter=delimiter)
    limit = row_limit
    # Check Headers
    if keep_headers:
        headers = next(input_file)
        writer.writerow(headers)
    # Writing into destination file
    for i, row in enumerate(input_file):
        if i + 1 > limit:
            current_row += 1
            limit = row_limit * current_row
            current_out_path = os.path.join(
                output_path, output_name_template % current_row
            )
            writer = csv.writer(open(current_out_path, "w"), delimiter=delimiter)
            if keep_headers:
                writer.writerow(headers)
        writer.writerow(row)


# The main function to call split_row function
def main():
    file_name = input("Input File Name: ")
    num_of_rows = input("Number of Rows: ")
    destination = input("Destination Path: ")
    try:
        split_rows(
            str(file_name), row_limit=int(num_of_rows), output_path=str(destination)
        )
        print("Done comeback soon!!!")

    except Exception as e:
        print("ERROR 404: Nothing Found")
        print(e)


if __name__ == "__main__":
    main()

"""
Example Usage-
`python csv_splitter.py`

- Input File Name: test
- Number of Rows: 500
- Done comeback soon!!!
"""
