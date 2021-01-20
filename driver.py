from bs4 import BeautifulSoup
import requests
import re
import lxml

from food import *

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')

soup = BeautifulSoup(URL.content, 'lxml')

list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')

for child in list_of_ingredients.children:

    item = child.text.split(' ')

    try:

        item[0] = (eval(item[0]) + eval(item[1]))
        remove_index_1 = item.pop(1)

        print(item)
    except (NameError, SyntaxError):
        item[0] = eval(item[0])
        print(item[0:])

    ingred_amount = item[0]
    ingred_unit = item[1]
    ingred_name = item[2:]
