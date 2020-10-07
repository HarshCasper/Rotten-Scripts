import requests

def NewsFromBBC():
     # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
    open_bbc_page = requests.get(main_url).json()
    articles = open_bbc_page['articles']
    results = []
    urls = []
    
    for ar in articles:
        results.append(ar['title'])
        urls.append(ar['url'])
    
    for i in range(len(results)):
        print(i+1, results[i])
        print("Link to the full article : " + urls[i] + '\n')
        

    
if __name__ == "__main__":
    NewsFromBBC()
