# A Python Script which can hash a string using a multitude of Hashing Algorithms like SHA256, SHA512 and more

import hashlib
import argparse
import sys


def main(text, hashType):
    encoder = text.encode("utf_8")
    myHash = ""

    if hashType.lower() == "md5":
        myHash = hashlib.md5(encoder).hexdigest()
    elif hashType.lower() == "sha1":
        myHash = hashlib.sha1(encoder).hexdigest()
    elif hashType.lower() == "sha224":
        myHash = hashlib.sha224(encoder).hexdigest()
    elif hashType.lower() == "sha256":
        myHash = hashlib.sha256(encoder).hexdigest()
    elif hashType.lower() == "sha384":
        myHash = hashlib.sha384(encoder).hexdigest()
    elif hashType.lower() == "sha512":
        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        print("[!] The script does not support this hash type")
        sys.exit(0)
    print("Your hash is: ", myHash)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text to hash")
    parser.add_argument("-t", "--text", dest="text", required=True)
    parser.add_argument("-T", "--Type", dest="type", required=True)
    args = parser.parse_args()

    txt = args.text
    hType = args.type
    main(txt, hType)
