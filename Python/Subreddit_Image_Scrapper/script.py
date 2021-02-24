# import modules
import requests
import json
import os


# Function for downloading images


def download_file(url_, i, limit, subreddit):
    r = requests.get(url_, stream=True)
    if r.ok:
        with open(f'Subreddit/{subreddit}/file{i}.png', 'wb') as file:
            for chunk in r.iter_content(1024 * 100):
                file.write(chunk)
        print(f'[{i}/{limit}] done')
    else:
        print(f'[{i}/{limit}] {r.status_code} whoops: Was not downloaded')
    # [#############]

# main function for the script


def main():
    subreddit = input("Please enter the subreddit you want to memes from: ")
    sort = input(
        "Please input sorting method here: (options: 'Top', 'Hot', 'new')")
    limit = eval(input("Number of memes: "))
    payload = {'sort': sort, 'limit': limit}
    print(payload)
    headers = {'user-agent': 'my-app/0.0.1'}
    # request for getting the urls of the subreddit
    url = f'https://www.reddit.com/r/{subreddit}.json'
    r = requests.get(url, params=payload, headers=headers)

    print(r.url)
    print(r.status_code)
    print(r.headers['content-type'])
    data1 = r.json()
    i = 0
    limit = int(data1["data"]["dist"])-2
    if not os.path.exists(f'Subreddit/{subreddit}'):
        os.makedirs(f'Subreddit/{subreddit}')
    for i in range(0, limit):
        # print(data1["data"]["children"][i]["data"]["url"]) <-- Name of the URL downloading images
        download_file(data1["data"]["children"][i]
                      ["data"]["url"], i, limit, subreddit)
        i = i + 1


if __name__ == '__main__':
    main()
