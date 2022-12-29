#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = "https://www.allrecipes.com/recipe/256007/best-scrambled-eggs/"
resp = requests.get(url)
def check_url(url,resp):
    
    resp = requests.get(url)
    
    if resp.status_code == 200:
        print(f'Url status code: {resp.status_code}')
        return (True,resp)
    else:
        print(f'Url status code: {resp.status_code}')
        return (False,) 

if check_url(url,resp) == True:
     
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.title.get_text()
    print('success')
else:
    print('failed')


#breakpoint()
