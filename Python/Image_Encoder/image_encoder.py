__author__ = "Sri Manikanta Palakollu"
__date__ = "08-07-2020"

import argparse
import base64
import json
import time

def b64_encode(source_filepath):
    with open(source_filepath, 'rb') as f:
        data = f.read()
    dest = open('ImageData/encodeData.json', 'r')
    flag = json.loads(dest.read())
    key = (str(int(time.time()))).decode('utf-8')
    d = {"data": base64.b64encode(data).decode(
        'utf-8'), "ext": source_filepath[source_filepath.index('.'):]}
    flag[key] = d
    dest.close()
    dest = open('ImageData/encodeData.json', 'w')
    json.dump(flag, dest)
    return key

def b64_decode(key, dest_path):
    source = open('ImageData/encodeData.json', 'r')
    flag = json.loads(source.read())
    name = key+str(flag[key]["ext"])
    dest = open(dest_path+name, 'wb')
    dest.write(base64.b64decode((flag[key]["data"]).encode('utf-8')))
    dest.close()
    return dest_path+name

parser = argparse.ArgumentParser()

parser.add_argument("-ie", "--ImageEncode", required=False, help="Image File for Encoding Purpose.")
parser.add_argument('-id', "--ImageDecode", required=False, help="Image File Decoding")
parser.add_argument('-k', "--Key", required=False, help="Key for Decoding the Image")

args = vars(parser.parse_args())

try:
    if(args['ImageEncode']):
        print("Key Value: {}".format(b64_encode(args['ImageEncode'])))
    else:
        b64_decode(args['Key'], args['ImageDecode'])
except Exception:
    print("Something went Wrong..!")