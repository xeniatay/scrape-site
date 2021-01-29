import requests
import time
from requests import Session

# 1. Script to scrape the urls in urls.txt
with open('./urls.txt') as f:
    urls = f.readlines()

text_blocks = []

session = Session()
session.cookies.clear()

for url in urls:
    url = url.strip()
    print(url)
    response = session.get(url)
    title = url.split('/')[-2]
    with open(f'./{title}.txt', 'w') as f:
        f.write(response.text)
    text_blocks.append(response.text)
