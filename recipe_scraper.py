#!/usr/bin/python3
import logging
import requests
from bs4 import BeautifulSoup

url = "https://www.allrecipes.com/recipe/256007/best-scrambled-eggs/"
resp = requests.get(url)

def check_website_support(url):
    """
    this function will check if the website can be parsed by the program.
    it will strip the url down, and valid against a whitelist style list
    the program should exit with a message that the url is unsupported
    """
    supported_websites = ['www.allrecipes.com']
    website = url.split('/')[2]
    if website in supported_websites:
        print(f'{website} is a supported website')
        return True
    else:
        print(f'{website} is not a supported website')

check_website_support(url)

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
