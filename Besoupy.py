from bs4 import BeautifulSoup
import requests
import re

URL = requests.get('https://www.bonappetit.com/recipe/duck-carnitas-tacos-with-radish-escabeche')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

Recipe_elem = soup.find('div', class_='sc-iQQKFN bKoSvH recipe__ingredient-list') 
Ingredient_amount = Recipe_elem.find('p', class_='sc-iCoHVE sc-fujyUd sc-ljpbHA inZljn jALVaM dYelzo')
Ingredient_elem = Recipe_elem.find('div', class_='sc-iCoHVE sc-fujyUd sc-jxFGMa inZljn jALVaM mYmiW')


# print(str(Recipe_elem))
grab_amount_class = re.findall("<div class=\"(.*)\">", str(Recipe_elem))

print(grab_amount_class)

# grab_unit_class = ''
# grab_name_class = ''

# print(Recipe_elem.prettify())
# print(Ingredient_amount, Ingredient_elem)

# match = soup.title.text # use this to get recipe name
# print(match)