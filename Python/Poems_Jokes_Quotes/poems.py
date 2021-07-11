# first install poetpy library using pip install poetpy
# using random to select a random poem
# import the required libraries
import poetpy
import random

try:
    print('Poem of which author you want to listen?')
    # taking the author name as input
    auth = input()
    
    # using the get_poetry() function to get poems
    poem = poetpy.get_poetry('author', auth, 'title,linecount')
    poems = poetpy.get_poetry('author', auth, 'lines')

    poem_len = len(poem)
    
    # selecting a random poem from the list of poems
    poem_no = random.randint(1, poem_len)

    # printing the different values realted to poem
    print("Title- ", poem[poem_no]['title'])
    print("No. of lines-", poem[poem_no]['linecount'])

    # print the peom
    poem_str = '\n'
    print("Poem-\n", poem_str.join(poems[poem_no]['lines']))

except Exception as e:
    pass
