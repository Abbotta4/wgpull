#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs

uri = 'https://wallhaven.cc/search?q=nature&categories=100&purity=100&atleast=2560x1440&sorting=random&order=desc'

try:
    r = requests.get(uri)
    if r.status_code is not 200:
        raise Exception('Bad request')
except Exception as e:
    print(e)
    exit(1)

soup = bs(r.text, 'html.parser')
uri = soup.main.ul.li.a['href']

try:
    r = requests.get(uri)
    if r.status_code is not 200:
        raise Exception('Bad request')
except Exception as e:
    print(e)
    exit(1)

soup = bs(r.text, 'html.parser')    
uri = 'https://' + soup.main.img['src'][2:]

try:
    r = requests.get(uri)
    if r.status_code is not 200:
        raise Exception('Bad request')
except Exception as e:
    print(e)
    exit(1)

filename = './wallpaper.' + uri[-3:]
print('saving ' + uri + ' to ' + filename)
with open(filename , 'wb') as f:
    f.write(r.content)
