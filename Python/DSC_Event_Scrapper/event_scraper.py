import csv
import sys
import requests

url = 'https://dsc.community.dev/api/event/?fields=id,chapter,event_type,event_type_title,title,status,start_date,end_date,start_date_naive,end_date_naive,url&status=Published&page=1'
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    header = ['title', 'chapter name', 'chapter country', 'chapter city', 'timezone',
              'start date', 'start time(local)', 'end date', 'end time(local)', 'event url', 'event type']
    writer.writerow(header)
    while 1:
        response = requests.get(url)
        # if exceptions raised quit the program
        try:
            response.raise_for_status()
        except:
            sys.exit()
        out = response.json()
        for i in out['results']:
            li = [i['title'], i['chapter']['title'], i['chapter']['country_name'], i['chapter']['city'], i['chapter']['timezone'], i['start_date_naive']
                  [:10], i['start_date_naive'][11:], i['end_date_naive'][:10], i['end_date_naive'][11:], i['url'], i['event_type_title']]
            writer.writerow(li)
        url = out['links']['next']
        # url = None when there is no further page
        if(url is None):
            break
