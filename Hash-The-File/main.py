import sys 
import hashlib

if len(sys.argv) < 2:
  print("Usage: python main.py filename")
  exit(1)

filenames = sys.argv[1:]

for filename in filenames:
  fd = open(filename, "r")
  content = fd.read()
  m = hashlib.md5(str.encode(content))
  print(m.hexdigest() + "  " + filename)
  fd.close()
