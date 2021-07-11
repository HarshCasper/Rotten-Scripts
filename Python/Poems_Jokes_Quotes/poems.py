import poetpy
import random

try:
    print('Poem of which author you want to listen?')
    auth = input()
    
    poem = poetpy.get_poetry('author', auth, 'title,linecount')
    poems = poetpy.get_poetry('author', auth, 'lines')

    poem_len = len(poem)
    
    poem_no = random.randint(1, poem_len)

    print("Title- ", poem[poem_no]['title'])
    print("No. of lines-", poem[poem_no]['linecount'])

    poem_str = '\n'
    print("Poem-\n", poem_str.join(poems[poem_no]['lines']))

except Exception as e:
    pass
