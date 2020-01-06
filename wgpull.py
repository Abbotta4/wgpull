#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs

uri = 'https://wallhaven.cc/search?q=nature&categories=100&purity=100&atleast=2560x1440&sorting=random&order=desc'

# requests.get with a status_code exception
def get(uri):
    try:
        r = requests.get(uri)
        if r.status_code is not 200:
            raise Exception('Bad request')
    except Exception as e:
        print(e)
        exit(1)
    return r
    
r = get(uri) # Load a results page
soup = bs(r.text, 'html.parser')
uri = soup.main.ul.li.a['href']
r = get(uri) # get the first link on the resutls page
soup = bs(r.text, 'html.parser')    
uri = 'https://' + soup.main.img['src'][2:]
r = get(uri) # download the source image
filename = './wallpaper.' + uri[-3:]

# save the file
print('saving ' + uri + ' to ' + filename)
with open(filename , 'wb') as f:
    f.write(r.content)
