
# import modules
import os
import requests


def download_file(url_, i, limit, subreddit):
    """
    Function for downloading images
    """
    request_sub = requests.get(url_, stream=True)
    if request_sub.ok:
        with open(f'Subreddit/{subreddit}/file{i}.png', 'wb') as file:
            for chunk in request_sub.iter_content(1024 * 100):
                file.write(chunk)
        print(f'[{i}/{limit}] done')
    else:
        print(f'[{i}/{limit}] {request_sub.status_code} whoops: Was not downloaded')


def main():
    """
    main function for the script
    """
    subreddit = input("Please enter the subreddit you want to memes from: ")
    sort = input(
        "Please input sorting method here: (options: 'Top', 'Hot', 'new')")
    limit = input("Number of memes: ")
    payload = {'sort': sort, 'limit': limit}
    print(payload)
    headers = {'user-agent': 'my-app/0.0.1'}
    # request for getting the urls of the subreddit
    url = f'https://www.reddit.com/r/{subreddit}.json'
    request_sub = requests.get(url, params=payload, headers=headers)

    print(request_sub.url)
    print(request_sub.status_code)
    print(request_sub.headers['content-type'])
    data1 = request_sub.json()
    i = 0
    limit = int(data1["data"]["dist"])-2
    if not os.path.exists(f'Subreddit/{subreddit}'):
        os.makedirs(f'Subreddit/{subreddit}')
    for i in range(0, limit):
        download_file(data1["data"]["children"][i]
                      ["data"]["url"], i, limit, subreddit)
        i = i + 1


if __name__ == '__main__':
    main()
