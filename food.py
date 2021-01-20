import os
class Recipe:

    num_of_ing = 0

    def __init__(self, name):
        
        self._name = name
        self._items = []

    @property
    def Items(self):
        return self._items

    @property.setter
    def Items(self, o)
        if type(o) is not list:
            raise TypeError(f'{type(o)} should be list')
        self._items = o

    def addItems(*args):
        for i in args:
            if type(i) is not Item:
                raise TypeError(f'{type(i)} should be item')
            self._items.append(i)

    @property
    def Name(self):
        return self._name

    @property.setter
    def Name(self, o):
        if type(o) is not str:
            raise TypeError(f'{type(o)} should be str')
        self._name = 0

    
    
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

class Item:
    def __init__(self, name, amount, measure):
        self._name = name
        self._amount = amount
        self._measure = measure

    @property
    def Name(self):
        return self._name

    @property
    def Amount(self):
        return self._amount
    
    @property
    def Measure(self):
        return self._measure

    @property.setter
    def Name(self, o):
        if type(o) is not str:
            raise TypeError(f'{type(o)} should be str')
        self._name = o

    @property.setter
    def Amount(self, o):
        if type(o) is not float:
            raise TypeError(f'{type(o)} should be float')
        self._amount = o
    
    @property.setter
    def Measure(self, o):
        if type(o) is not str:
            raise TypeError(f'{type(o)} should be str')
        self._measure = o

ing_1 = Recipe('1', 'Cups', 'Cheddar')
ing_2 = Recipe('1', 'Cups', 'Cheddar')
ing_str_1 = 1, 'tablespoon', 'olive', 'oil'

print(Recipe.from_string(ing_str_1).full_ingredient)
print(Recipe.from_string(ing_str_2).full_ingredient)
print(Recipe.from_string(ing_str_3).full_ingredient)
print(Recipe.from_string(ing_str_4).full_ingredient)

class Instructions:
    pass # watch Python OOP 4 for subclass inheritance when you get back to here
