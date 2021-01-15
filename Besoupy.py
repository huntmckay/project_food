from bs4 import BeautifulSoup
import requests
import re

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')


ingred_amount = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-amount')
ingred_unit = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-unit')
ingred_name = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-name')

for child in list_of_ingredients.children:
    # print(child.text.split(' '))

    yeet = child.text.split(' ')
    print(yeet[0])