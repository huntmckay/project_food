# I can do this
import os
class Recipe:

    num_of_ing = 0

    def __init__(self, amount, unit, name):
        
        #want to move float/eval logic to its own classmethod
        self.amount = float(eval(amount))
        self.unit = unit
        self.name = name

    @property #allows me to access this method as an attribute
    def full_ingredient(self):
        return '{} {} {}'.format(self.amount, self.unit, self.name)
    
    @classmethod
    def from_string(cls, ing_str):
        amount, unit, name = ing_str.split('-')
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

# repr(ing_1)
# str(ing_1)
print(Recipe.from_string(ing_str_1).full_ingredient)
print(Recipe.from_string(ing_str_2).full_ingredient)
print(Recipe.from_string(ing_str_3).full_ingredient)
print(Recipe.from_string(ing_str_4).full_ingredient)

class Instructions:
    pass # watch Python OOP 4 for subclass inheritance when you get back to here