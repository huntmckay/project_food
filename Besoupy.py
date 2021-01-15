from bs4 import BeautifulSoup
import requests
import re

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

ingredients = soup.find('ul', class_='wprm-recipe-ingredients')
for string in ingredients:
    print(repr(string.text))

# grab_title = soup.title.string