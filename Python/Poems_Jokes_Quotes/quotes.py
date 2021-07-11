# first install quote library using pip install quote 
# then import it using from quote import quote
from quote import quote
# using random library for getting a random quote
import random

try:
    print("Tell me the author or person name?")
    
    # taking the author/person name as input
    q_author = input()
    
    # getting the quotes
    quotes = quote(q_author)
    
    # selecting a random quote 
    quote_no = random.randint(1, len(quotes))
    
    # displaying the quote with author name
    print("Author: ", quotes[quote_no]['author'])
    print("-->", quotes[quote_no]['quote'])

except Exception as e:
    pass
