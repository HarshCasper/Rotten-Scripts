import requests
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree

res = requests.get("https://github.com/HarshCasper/Rotten-Scripts")

tree = parse_html_bytes(res.content, res.headers.get("content-type"))

links = set(find_links_tree(tree))
print(links)
