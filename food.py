# I can do this
import os
class Recipe:

    def __init__(self, amount, unit, name):
        
        #want to move float/eval logic to its own classmethod
        self.amount = amount
        self.unit = unit
        self.name = name

    def scrapeurl(self, list_of_ingredients):
        URL = requests.get('https://www.thewholesomedish.com/the-best-classic-chili/')
        soup = BeautifulSoup(URL.content, 'lxml')
        list_of_ingredients = soup.find('ul', class_='wprm-recipe-ingredients')
        return list_of_ingredients

    @property
    def get_item(self):

        for child in self.list_of_ingredients.children:

            item = child.text.split(' ')
            try:
                # print('ITEM_0', '-', item[0], '   ', 'ITEM_1', '-', item[1]) #future debug
                item[0] = (eval(item[0]) + eval(item[1]))
                remove_index_1 = item.pop(1)
                print(item)
                # print('removed', remove_index_1) # future debug

                # print('this is new item zero', '-', item[0]) #future debug
            except (NameError, SyntaxError):
                item[0] = eval(item[0])
                print(item[0:])

            self.amount = item[0]
            self.unit = item[1]
            self.name = item[2:]

        return '{} {} {}'.format(self.amount, self.unit, self.name)

    
    @classmethod
    def from_string(cls, ing_str):
        amount, unit, name = ing_str.split('-')
        return cls(amount, unit, name)

    @classmethod
    def from_list(cls, ing_list):
        amount, unit, name = ing_str.list()
        return cls(amount, unit, name)

    def __repr__(self):
        return "Recipe('{}', '{}', '{}')".format(self.amount, self.unit, self.name)

    def __str__(self):
        return '{} {} {}'.format(int(self.amount), self.unit, self.name)

    def __add__(self, other):
        return self.amount + other.amount
    #dunder for adding use later for comparison +
    #print(ing_1 + ing_2)

    # def __len__(self):
    #     return len(self.unit)
    # not sure how i would use but cool anyway look up "special methods"
    # print(len(ing_1))

ing_1 = Recipe('1', 'Cups', 'Cheddar')
ing_2 = Recipe('1', 'Cups', 'Cheddar')

ing_str_1 = '1-cups-cheddar'
ing_str_2 = '2-tbsp-soy sauce'
ing_str_3 = '5.5-lbs-chicken'
ing_str_4 = '1/2-cups-milk'

# ing_str_1 = [1, 'tablespoon', 'olive', 'oil']
# ing_str_2 = [1, 'medium', 'yellow', 'onion', '-diced']
# ing_str_3 = [1, 'pound', '90%', 'lean', 'ground', 'beef']
# ing_str_4 = [2.5, 'tablespoons', 'chili', 'powder']
# [2, 'tablespoons', 'ground', 'cumin']
# [2, 'tablespoons', 'granulated', 'sugar']
# [2, 'tablespoons', 'tomato', 'paste']
# [1, 'tablespoon', 'garlic', 'powder']
# [1.5, 'teaspoons', 'salt']
# [0.5, 'teaspoon', 'ground', 'black', 'pepper']
# [0.25, 'teaspoon', 'ground', 'cayenne', 'pepper*', '-optional']
# [1.5, 'cups', 'beef', 'broth']
# [1, '(15', 'oz.)', 'can', 'petite', 'diced', 'tomatoes']
# [1, '(16', 'oz.)', 'can', 'red', 'kidney', 'beans,', 'drained', 'and', 'rinsed']
# [1, '(8', 'oz.)', 'can', 'tomato', 'sauce']

# repr(ing_1)
# str(ing_1)
print(Recipe.from_string(ing_str_1).full_ingredient)
print(Recipe.from_string(ing_str_2).full_ingredient)
print(Recipe.from_string(ing_str_3).full_ingredient)
print(Recipe.from_string(ing_str_4).full_ingredient)

class Instructions:
    pass # watch Python OOP 4 for subclass inheritance when you get back to here