from tqdm import tqdm
import requests
import html
import sys


def download(url):
    source = requests.get(url).text
    source_cleaned = html.unescape(source).split()
    for item in source_cleaned:
        if "dms.licdn.com" in item:
            download_link = item.split(',')[0].split('"src":')[1][1:-1]
            r = requests.get(download_link, stream=True)
            total_size_in_bytes = int(r.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            progress_bar = tqdm(total=total_size_in_bytes,
                                unit='iB', unit_scale=True)
            with open('test.mp4', 'wb') as file:
                for data in r.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("ERROR, something went wrong")


if __name__ == "__main__":
    download(sys.argv[1])
