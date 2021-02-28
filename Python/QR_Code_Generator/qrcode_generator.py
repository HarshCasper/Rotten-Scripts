import pyqrcode
import csv
import argparse


def generate_qr_code(input_file):
    """   
    :param input_file: str
    :return: None
    """
    with open(input_file, "r") as cf:
        csv_reader = csv.reader(cf)
        for row in csv_reader:
            qrcode = pyqrcode.create(row[1])
            qrcode.png(str(row[0]) + ".png", scale=6)
    print("finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--f", type=str, required=True,
                        help="specify file with data to be encoded.")
    args = parser.parse_args()
    input_filename = args.f
    generate_qr_code(input_filename)
