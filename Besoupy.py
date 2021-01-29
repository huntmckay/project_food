from bs4 import BeautifulSoup
import requests
import re
import lxml

URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')


# with open('URL') as html_file:
soup = BeautifulSoup(URL.content, 'lxml')

list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')

for child in list_of_ingredients.children:
    length_of_list = len(list_of_ingredients)

    # print(length_of_list)
    item = child.text.split(' ')

    # evaluate the number
    # then compare check to see if it failed the eval because its a string
    # then add index_0 and index_1
    # if type(eval(item[0])) == int or float : print('yeeyee')
    # elif type(eval(item[0])) != int or float : print('naynay')
    myDict = {}
    myDict['item'] = 'cow'
    try:
        # print('ITEM_0', '-', item[0], '   ', 'ITEM_1', '-', item[1]) #future debug
        item[0] = (eval(item[0]) + eval(item[1]))
        remove_index_1 = item.pop(1)
        # print(item)
        myDict['item'].append(item)
        # print('removed', remove_index_1) # future debug
        
        # print('this is new item zero', '-', item[0]) #future debug
    except (NameError, SyntaxError):
        item[0] = eval(item[0])
        # print(item[0:])
        
        myDict['item'].append(item)
    # print(child.text.split(' '))
    print(myDict)
    #this is how i want the class output to be
    ingred_amount = item[0]
    ingred_unit = item[1]
    ingred_name = item[2:]