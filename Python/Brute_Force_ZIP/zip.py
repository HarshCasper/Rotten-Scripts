# By CYB3R G0D
#
#
# pip3 install tqdm
from tqdm import tqdm
import zipfile
import sys


# the wordlist path (in current dir)
wordlist = 'rockyou.txt'
# the zip file path
file = input('zip file directory: ')
file = zipfile.ZipFile(file)
n_words = len(list(open(wordlist, 'rb')))
# print total number of passwords in the list
print('Total passwords to test:', n_words)
with open(wordlist, 'rb') as wordlist:
    for word in tqdm(wordlist, total=n_words, unit='word'):
        try:
            file.extractall(pwd=word.strip())
        except RuntimeError:
            print('[*] Trying', word.decode().strip())
        else:
            print('[+] Password found:', word.decode().strip())
            sys.exit(1)
