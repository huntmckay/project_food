from bs4 import BeautifulSoup
import requests
import re
import lxml

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')


# ingred_amount = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-amount')
# ingred_unit = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-unit')
# ingred_name = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-name')
for child in list_of_ingredients.children:
    length_of_list = len(list_of_ingredients)

    # print(length_of_list)
    item = child.text.split(' ')

    print(child.text.split(' '))