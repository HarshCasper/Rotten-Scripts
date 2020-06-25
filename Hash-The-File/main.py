import sys 
import hashlib

if len(sys.argv) < 2:
  print("Usage: python main.py filename")
  exit(1)

filenames = sys.argv[1:]

m = hashlib.md5()
m.update(b"Sankey")

print(m.hexdigest())
