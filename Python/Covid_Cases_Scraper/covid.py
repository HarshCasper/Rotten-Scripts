import bs4
import requests

try:
    print('For which region you want to see the COVID-19 cases?\nPlease write below!\n'
         'Example:\noverall/total/worldwide/all - for overall cases in the world\ncountry/COunTRY/COUNTRY/Country - for any specific country')
    
    c_query = input().lower()
    print()
    
    if 'overall' in c_query or 'over all' in c_query or 'world' in c_query or 'total' in c_query or 'worldwide' in c_query or 'all' in c_query:
        def world_cases():
            
                url = 'https://www.worldometers.info/coronavirus/'
                
                info_html = requests.get(url)
                
                info = bs4.BeautifulSoup(info_html.text, 'lxml')
                
                info2 = info.find('div', class_='content-inner')
                
                new_info = info2.findAll('div', id='maincounter-wrap')
                
                print('Worldwide Covid-19 information--')

                for i in new_info:
                    head = i.find('h1', class_=None).get_text()
                    counting = i.find('span', class_=None).get_text()
                    print(head, "", counting)

        world_cases()

    elif 'country' in c_query or 'specific country' in c_query:
        def country_cases():

                print('Write the country name?')
                
                c_name = input().lower()
                print()
                
                c_url = f'https://www.worldometers.info/coronavirus/country/{c_name}/'
                
                data_html = requests.get(c_url)
                
                c_data = bs4.BeautifulSoup(data_html.text, 'lxml')
                
                new_data = c_data.find('div', class_='content-inner').findAll('div', id='maincounter-wrap')
                print(f'Covid-19 information for {c_name.capitalize()}--')

                for j in new_data:
                    c_head = j.find('h1', class_=None).get_text()
                    c_counting = j.find('span', class_=None).get_text()
                    print(c_head, "", c_counting)

        country_cases()

    else:
        print("There is something wrong. Please try again.")

except Exception as e:
    pass
