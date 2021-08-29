# Machine Learning-based News Scrapper

This is a Machine Learning-based News Scrapper. It makes use of the Machine Learning models to extract the most relevant news articles from the web, according to the News URL passed as a user input. Under the hood it makes use of the Google Search API and Cosine Similarity to find the most relevant news articles.

## Setup instructions

1.Install the Python dependencies:

  ```sh
  pip install -r requirements.txt
  ```

2.Run the Script:

  ```sh
  python3 machine_learning_news_scrapper.py <NEWS_URL>
  ```

  You need to replace the `<NEWS_URL>` with the URL of the news you want to scrape, similar news articles for.

## Example

Let's push the following URL to the script:

```sh
python3 machine_learning_news_scrapper.py https://www.aninews.in/news/world/asia/covid-19-sri-lanka-re-opens-for-indian-travellers20210828185136
```

We will retrieve the following output:

```sh
News Link  Similarity Score
https://timesofindia.indiatimes.com/world/south-asia/covid-19-sri-lanka-re-opens-for-indian-travellers/articleshow/85716661.cms 99.30332922
https://m.timesofindia.com/world/south-asia/covid-19-sri-lanka-re-opens-for-indian-travellers/amp_articleshow/85716661.cms 99.30332922
https://english.lokmat.com/international/covid-19-sri-lanka-re-opens-for-indian-travellers/ 99.4162306
https://www.tourmyindia.com/blog/sri-lanka-tourism-update/ 65.41847315
https://www.india.com/business/international-flights-latest-news-today-28-august-2021-sri-lanka-reopens-borders-with-india-starts-regular-flights-from-9-indian-cities-full-details-4919999/ 87.44739827
```

## Author(s)

[Aditi Sneh](https://github.com/aditisneh)
