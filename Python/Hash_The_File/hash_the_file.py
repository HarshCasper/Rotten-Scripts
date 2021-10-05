import sys
import hashlib

# Some functions may not be available in some
# systems and in python2

HASH_MAP = {
    "--md5": hashlib.md5,
    "--sha1": hashlib.sha1,
    "--sha224": hashlib.sha224,
    "--sha256": hashlib.sha256,
    "--sha384": hashlib.sha384,
    "--sha512": hashlib.sha512,
    "--blake2b": hashlib.blake2b,
    "--blake2s": hashlib.blake2s,
    "--sha3_224": hashlib.sha3_224,
    "--sha3_256": hashlib.sha3_256,
    "--sha3_384": hashlib.sha384,
    "--sha3_512": hashlib.sha512,
    "--shake_128": hashlib.shake_128,
    "--shake_256": hashlib.shake_256,
}


def help():
    print("Usage: python main.py [--<method>] filenames")
    print("Available hash methods")
    for method in HASH_MAP:
        print("   ", method)


if len(sys.argv) < 2:
    help()
    sys.exit(0)

offset = 1
flag = False
potential_flag = sys.argv[1]

if potential_flag[:2] == "--":
    offset = 2
    flag = potential_flag

if flag:
    if flag == "--help":
        help()
        exit(0)
    try:
        hsh = HASH_MAP[flag]
    except KeyError:
        print("Invalid flag", flag)
        sys.exit(1)
    except:
        raise
else:
    print("No method specified. Using md5.")
    hsh = hashlib.md5

filenames = sys.argv[offset:]

if len(filenames) == 0:
    help()
    sys.exit(1)

for filename in filenames:
    fd = open(filename, "r")
    content = fd.read()
    m = hsh(str.encode(content))
    print(m.hexdigest() + "  " + filename)

    fd.close()
