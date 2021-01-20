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

    # evaluate the number
    # then compare check to see if it failed the eval because its a string
    # then add index_0 and index_1
    # if type(eval(item[0])) == int or float : print('yeeyee')
    # elif type(eval(item[0])) != int or float : print('naynay')

    try:
        # print('ITEM_0', '-', item[0], '   ', 'ITEM_1', '-', item[1]) #future debug
        item[0] = (eval(item[0]) + eval(item[1]))
        remove_index_1 = item.pop(1)
        print(item)
        print('removed', remove_index_1)
        
        # print('this is new item zero', '-', item[0]) #future debug
    except (NameError, SyntaxError):
        item[0] = eval(item[0])
        print(item[0:])
    # print(child.text.split(' '))