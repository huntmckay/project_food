import requests
from bs4 import BeautifulSoup
import re

URL = 'https://happymoneysaver.com/cilantro-lime-chicken/'
# URL = 'https://happymoneysaver.com/freezer-chicken-taquitos-with-cream-cheese/'
# URL = 'https://www.budgetbytes.com/chicken-mandarin-salad-simple-sesame-dressing/'


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


recipe_elems = soup.find_all('li', class_='wprm-recipe-ingredient')
ingredients = len(recipe_elems)
x = 0
big_dict = {}

while x < ingredients:
    
    amount_elem = recipe_elems[x].find('span', class_ = 'wprm-recipe-ingredient-amount')
    unit_elem = recipe_elems[x].find('span', class_ = 'wprm-recipe-ingredient-unit')
    name_elem = recipe_elems[x].find('span', class_ = 'wprm-recipe-ingredient-name')


    if amount_elem.text == '':
        amount = ''
        pass
    else:
        amount = eval(amount_elem.text)
        pass
        
    if unit_elem is None:
        unit = ''
        pass
    else:
        unit = unit_elem.text

    if name_elem is None:
        name = ''
        pass
    else:
        name = name_elem.text


    print(amount,unit,name) 
    x += 1





    big_dict = { 'chicken':2.5 }

    2.5 lbs

