## Twitter Images Downloader

This script downloads images from given user's recent tweets and also creates a CSV file with `Tweet URL`, `Image ID`, `Image URL` columns.

### Instructions

1. Add env variables:

   1. Create a new file named `.env`
   2. Copy the contents of `.env.example` to `.env`
   3. Paste your `CONSUMER_KEY` and `CONSUMER_SECRET` in `.env` (Get them [here](https://developer.twitter.com/))

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

3. Run the script and give inputs as asked.

```sh
$ python3 images_download.py
```

### Author

[Yash Kandalkar](https://github.com/YashKandalkar)
