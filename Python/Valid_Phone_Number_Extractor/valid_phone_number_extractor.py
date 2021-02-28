import re
import argparse

parser = argparse.ArgumentParser(
    description='Find mobile or phone numbers from input text file.')

# list of cli arguments/flags
parser.add_argument('--mobile', '-m', help='Extract mobile numbers only.')
parser.add_argument('--phone', '-p', help='Extract Phone Numbers only.')
parser.add_argument(
    '--all', '-a', help='Extract both Mobile Numbers and Phone Numbers.')
parser.add_argument('--output', '-o', help='Name of output file.')

args = parser.parse_args()

mobile_num = re.compile(r'\b\d{5}-\d{5}\b')     # REGEX for mobile numbers
phone_num = re.compile(r'\b\d{3}-\d{7}\b')      # REGEX for phone numbers


def find_valid_mobile_number():
    input_file = open(args.mobile, 'r')             # Open input file
    # Open output file
    if args.output:
        output_file = open(args.output, 'w')
    else:
        output_file = open('valid_mobile_numbers.txt', 'w')
    output_file.write('Valid Mobile Numbers\n')
    # Valid mobile numbers
    for line in input_file:
        valid_mobile_num = mobile_num.findall(line)
        for mnum in valid_mobile_num:
            output_file.write(mnum+'\n')
    # Close files
    input_file.close()
    output_file.close()


def find_valid_phone_number():
    input_file = open(args.phone, 'r')             # Open input file
    # Open output file
    if args.output:
        output_file = open(args.output, 'w')
    else:
        output_file = open('valid_phone_numbers.txt', 'w')
    output_file.write('Valid Phone Numbers\n')
    # Valid phone numbers
    for line in input_file:
        valid_phone_num = phone_num.findall(line)
        for pnum in valid_phone_num:
            output_file.write(pnum+'\n')
    # Close files
    input_file.close()
    output_file.close()


def find_all_valid_number():
    input_file = open(args.all, 'r')             # Open input file
    # Open output file
    if args.output:
        output_file = open(args.output, 'w')
    else:
        output_file = open('valid_numbers.txt', 'w')
    output_file.write('Valid Mobile Numbers\n')
    # Valid mobile numbers
    for line in input_file:
        valid_mobile_num = mobile_num.findall(line)
        for mnum in valid_mobile_num:
            output_file.write(mnum+'\n')
    output_file.write('\nValid Phone Numbers\n')
    input_file = open(args.all, 'r')             # Open input file
    # Valid phone numbers
    for line in input_file:
        valid_phone_num = phone_num.findall(line)
        for pnum in valid_phone_num:
            output_file.write(pnum+'\n')
    # Close files
    input_file.close()
    output_file.close()


def main():
    if args.mobile is not None:
        find_valid_mobile_number()
    elif args.phone is not None:
        find_valid_phone_number()
    elif args.all is not None:
        find_all_valid_number()
    else:
        print('Oh well ; you forgot to enter arguments.')


if __name__ == '__main__':
    main()
