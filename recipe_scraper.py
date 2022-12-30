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

def check_url(url):
    
    resp = requests.get(url)
    
    if resp.status_code == 200:
        print(f'Url status code: {resp.status_code}')
        return (True)
    else:
        print(f'Url status code: {resp.status_code}')
        return (False,) 


def scrape_recipe(url):
    
    ingredients = []
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.title.get_text()
    name = soup.title.name     
    s = soup.find('div', id="mntl-structured-ingredients_1-0")
    tags = s.find_all('li')

    print(title)
    for tag in tags:
        clean_tag = tag.text.strip('\n')
        a = clean_tag.split(' ')
        my_dict = { a[0]:a[1:] }
        ingredients.append(my_dict)

    for i in ingredients:
        print(i)

scrape_recipe(url)
