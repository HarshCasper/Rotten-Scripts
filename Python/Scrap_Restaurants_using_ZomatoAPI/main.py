import os 
import requests
import csv
from dotenv import load_dotenv

def start_scrap(key) :
  file_name = input(
      "Enter the file name to save Restaurants List with extension name .csv : ")
  with open(file_name, "a", newline='') as fp:
      wr = csv.writer(fp, dialect='excel')
      # Change City with &q=""
      url = "https://developers.zomato.com/api/v2.1/search?entity_id=4&entity_type=city&q=Mumbai&start=1"
      header = {"Accept": "application/json", "user-key": key,
                "User-agent": "curl/7.43.0"}  # Replace API-KEY with your Zomato API, API Limit: 1000 Calls/day
      resp = requests.get(url, headers=header).json()
      for i in range(0, 20):
          rest = resp['restaurants'][i]
          res_id = rest['restaurant']['id']
          name = rest['restaurant']['name']
          locality = rest['restaurant']['location']['locality']
          cuisines = rest['restaurant']['cuisines']
          average_cost_for_two = rest['restaurant']['average_cost_for_two']
          rating = rest['restaurant']['user_rating']['aggregate_rating']
          votes = rest['restaurant']['user_rating']['votes']
          list_ = [res_id, name, locality, cuisines,
                  average_cost_for_two, rating, votes]
          wr.writerow(list_)


if __name__ == '__main__':
  load_dotenv()
  projectAPIKey  =os.getenv('projectKey')
  start_scrap(projectAPIKey)
