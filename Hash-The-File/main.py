import sys 
import hashlib

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
  "--shake_256": hashlib.shake_256
}

if len(sys.argv) < 2:
  print("Usage: python main.py filename")
  exit(1)

offset = 1
flag = False
potential_flag = sys.argv[1]

if potential_flag[:2] == "--":
  offset = 2
  flag = potential_flag

if flag:
  hsh = HASH_MAP[flag]
else:
  hsh = hashlib.md5

filenames = sys.argv[offset:]

for filename in filenames:
  fd = open(filename, "r")
  content = fd.read()
  m = hsh(str.encode(content))
  print(m.hexdigest() + "  " + filename)

  fd.close()
