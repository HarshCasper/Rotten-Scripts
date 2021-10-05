import json
import sys
import yaml
import argparse

# Code to add the cli
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--jsonfile", required=True, help="JSON file ")
args = vars(parser.parse_args())


json_file = args["jsonfile"]

# End the program if the file extension is incorrect
if json_file.endswith("json") is False:
    sys.exit("Please enter a json file only")

# Reading the json file and ensuring the formatting
with open(json_file, "r") as file_object:
    try:
        data = json.load(file_object)
    except:
        sys.exit(" Please check the formatting of your json file")

# Extracting the name of the file to make sure the yaml file has the same name
file_name = json_file.split(".")[0]
file_in_yaml_format = file_name + ".yaml"

# Here the sorted_keys pararmeter is kept false to maintain the order of keys as present in the input json file.
with open(file_in_yaml_format, "w") as file_object_2:
    yaml.dump(data, file_object_2, sort_keys=False)


print("Your yaml file has been created successfully")
