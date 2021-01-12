import requests
from bs4 import BeautifulSoup

# URL = 'https://happymoneysaver.com/cilantro-lime-chicken/'
# URL = 'https://happymoneysaver.com/freezer-chicken-taquitos-with-cream-cheese/'
# URL = 'https://www.budgetbytes.com/chicken-mandarin-salad-simple-sesame-dressing/'
URL = 'https://www.bonappetit.com/recipe/duck-carnitas-tacos-with-radish-escabeche'

page = requests.get(URL)
# if page.status_code !=200:
#     raise ApiError('POST /tasks/ {}'.format(resp.status_code))

soup = BeautifulSoup(page.content, 'html.parser')

x = 0
recipe_elems = soup.find_all('li', class_='wprm-recipe-ingredient')

ingredients = len(recipe_elems)

print(recipe_elems)