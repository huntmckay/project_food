from bs4 import BeautifulSoup
import requests
import re

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')


# ingred_amount = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-amount')
# ingred_unit = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-unit')
# ingred_name = list_of_ingredients.find('span', class_='wprm-recipe-ingredient-name')

for child in list_of_ingredients.children:
    length_of_list = len(list_of_ingredients)

    x = 0
    # print(child.text.split(' '))
    item = child.text.split(' ')
    # while x < length_of_list:
    #     try:
    #         amount = eval(item[0])
    #         print(amount)
    #         pass
    #     except:
    #         print(type(item[0]


    # while x < ingredients:
    # if ita[0] and ita[1] == int:
    #     amount = eval(ita[0] + ita[1])
    # else:
    #     amount = eval(ita[0])
    # print(amount)
    # print(ita[0], ita[1:3])
    print(child.text.split(' '))