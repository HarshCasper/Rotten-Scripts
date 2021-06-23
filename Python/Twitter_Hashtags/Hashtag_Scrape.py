import snscrape.modules.twitter as sntweets
import csv


tag = input("Enter a hashtag: #")
max_count = int(input("Enter maximum number of tweets to be listed: "))
file_name = input("Enter the name of file to store the tweet info: ")

print("Creating a .csv file regarding the hashtag....")

tweets_list = []
count = 0

for i in sntweets.TwitterSearchScraper("#" + tag).get_items():
    tweets_list.append([i.id, i.username, i.date, i.content, i.url])
    count += 1

    if count == max_count:
        break


if count != 0:
    header_list = ["Id", "Username", "Date and Time", "Tweet", "Url"]

    with open(file_name + ".csv", "a", encoding="utf-8") as csv_f:
        csv_pointer = csv.writer(csv_f, delimiter=",")
        csv_pointer.writerow(header_list)
        csv_pointer.writerows(tweets_list)

    print(f"Done! Check your directory for {file_name}.csv file!")

else:
    print("No tweets available for this hashtag")
