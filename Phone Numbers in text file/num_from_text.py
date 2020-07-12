import re
import argparse

parser = argparse.ArgumentParser(description='Find mobile or phone numbers from input text file.')

# list of cli arguments/flags
parser.add_argument('--mobile', '-m', help='Extract mobile numbers only.')
parser.add_argument('--phone', '-p', help='Extract Phone Numbers only.')
parser.add_argument('--all', '-a', help='Extract both Mobile Numbers and Phone Numbers.')

args = parser.parse_args()

mobile_num = re.compile(r'\b\d{5}-\d{5}\b')     # REGEX for mobile numbers
phone_num = re.compile(r'\b\d{3}-\d{7}\b')      # REGEX for phone numbers

input_file = open('kjv10.txt', 'r')             # Open input file
output_file = open('valid_number.txt', 'w')     # Open output file

output_file.write('Valid Mobile Numbers\n')
# Valid mobile numbers
for line in input_file:
    valid_mobile_num = mobile_num.findall(line)
    for mnum in valid_mobile_num:
        output_file.write(mnum+'\n')

output_file.write('\nValid Phone Numbers\n')
# Valid phone numbers
for line in input_file:
    valid_phone_num = phone_num.findall(line)
    for pnum in valid_phone_num:
        output_file.write(pnum+'\n')

# Close files
input_file.close()
output_file.close()