from bs4 import BeautifulSoup
import requests
import re

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

# print(str(Recipe_elem))
# grab_amount_class = re.findall("<div class=\"(.*)\">", str(Recipe_elem))

# print(grab_amount_class)

Recipe_elems = soup.find_all(id ='wprm-recipe-container-8547')

# for string in soup.stripped_strings:
#     print(repr(string))

grab_title = soup.title.string
a = class_='wprm-recipe-ingredient-name'
b = class_='wprm-recipe-ingredient-unit'
c = class_='wprm-recipe-ingredient-amount'
list_grab = soup.find_all(["a", "b", "c"])
print(list_grab)

# print(ingred_amount.content)
# print(str(ingred_amount,ingred_unit,ingred_unit))
# Ingredient_amount = Recipe_elem.find('p', class_='sc-iCoHVE sc-fujyUd sc-ljpbHA inZljn jALVaM dYelzo')
# Ingredient_elem = Recipe_elem.find('div', class_='sc-iCoHVE sc-fujyUd sc-jxFGMa inZljn jALVaM mYmiW')

# grab_unit_class = ''
# grab_name_class = ''