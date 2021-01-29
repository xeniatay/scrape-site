import requests
import time
import bs4

# 2. Script to parse the output.html because it was too big to manually parse in the console
print('Opening output.html...')
with open('./output.html') as f:
    monster = f.read()

print('Beautiful souping...')
text_blocks = []
soup = bs4.BeautifulSoup(monster, features="html.parser")

print('Finding #wtr-content...')
for el in soup.find_all(id='wtr-content'):
    print(f'{el}')
    text_blocks.append(el.text)

with open('./output.txt', 'w') as f:
    f.write('\n'.join(text_blocks))
