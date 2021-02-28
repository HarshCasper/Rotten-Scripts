# import the lorem module from lorem_text
from lorem_text import lorem

# Provide the number of paragrpahs you want
paragraph_length = int(input("Enter the length of paragraph you want: "))

# Store it in a variable, lorem.paragraphs() is used to generate the paragraphs
se = lorem.paragraphs(paragraph_length)

# Finally print the paragraphs
print(se)
