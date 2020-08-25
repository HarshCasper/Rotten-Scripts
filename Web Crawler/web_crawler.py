# pip install bs4
# import the packages

import requests
import re
from bs4 import BeautifulSoup

# link for scraping data
# perform a get request for the link
source = requests.get('https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_pgn=1').text    

def crawler():

    # parsing it with Beautiful Soup
    soup = BeautifulSoup(source, 'lxml')
    # declaring items variable to make it more concise for a particular portion 
    items = soup.find('li', class_='s-item')


    # six categories for the particular product are mention for scrapping purpose
    # finds all the item from the list and store it 
    for items in soup.find_all('li', class_='s-item'):

        # title of the product
        try:  
            item_title = items.find('h3', class_='s-item__title').text
        except Exception as e:
            item_title = 'None'
        print(item_title)

        # price of the product
        try:
            item_price = items.find('span', class_='s-item__price').text
        except Exception as e:
            item_price = 'None'
        print(item_price)

        # shipping price information
        try:
            item_shipping = items.find('span', class_='s-item__shipping s-item__logisticsCost').text
        except Exception as e:
            item_shipping = 'None'
        print(item_shipping)
           
        # rating of the product
        try:
            item_stars = items.find('span', class_='clipped').text.split(' ')[0]
        except Exception as e:
            item_stars = 'None'
        print(item_stars)
        
        # checks whether quantity has been sold or not
        try:
            item_qty_sold = items.find('span', class_='s-item__hotness s-item__itemHotness').text.split(' ')
            
            if item_qty_sold[1] == 'sold':
                item_qty_sold = item_qty_sold[0]
            else:
                item_qty_sold = 0
        except Exception as e:
            item_qty_sold = 'None' 
        print(item_qty_sold)

        # retrieving the link of the product
        try:
            item_link = items.find('a', class_='s-item__link')['href']
        except Exception as e:
            item_link = 'None'
        print(item_link,"\n")
        
        print()

# call the function    
if __name__ == '__main__':
    try:
        crawler()
    except:
        print("\nError")
