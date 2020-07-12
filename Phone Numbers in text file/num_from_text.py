import re

mobile_num = re.compile(r'\b\d{5}-\d{5}\b')
phone_num = re.compile(r'\b\d{3}-\d{7}\b')

output_file = open('valid_mobile_number.txt', 'w')

with open("kjv10.txt", "r") as input_file:
    for line in input_file:
        valid_mobile_num = mobile_num.findall(line)
        valid_phone_num = phone_num.findall(line)
        for mnum in valid_mobile_num:
            print(mnum)
            output_file.write(mnum)
        for pnum in valid_phone_num:
            print(pnum)
            output_file.write(pnum)

input_file.close()
output_file.close()