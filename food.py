from bs4 import BeautifulSoup
import requests
import re
import lxml

class Recipe:
    def __init__(self, name, url):
        
        self.Name = name

        self._url = url
        self._items = []
        self._measure = [
            'pinch',
            'cup',
            'spoon',
            'can',
            'tsp',
            'tbsp',
            'lb',
            'pound',
            'kilo',
            'gram',
            'medium',
            'large',
            'small',
            'kg',
            'oz',
            'fl'
        ]
        self._load_all()
    
    def _load_all(self):
        results = requests.get(self._url)
        soup = BeautifulSoup(results.content, 'lxml')

        items = soup.find('ul', class_='wprm-recipe-ingredients')

        for i in items.children:
            item = i.text.split(' ')

                # Here we are going to loop and look for known units of measure
            ind = 0
            desc = ''
            for k in range(0,len(item)):
                for m in self._measure:
                    if m in item[k]:
                        # print(f'position {k} in {item} is a unit of measure')
                        ind = k

                if ind > 1:
                    item[1:ind]
                    for i in item[1:ind]:
                        desc += i

            if ind == 1:
                amount = eval(item[0])
            elif desc != '':
                amount = eval(item[0])
            else:
                amount = (eval(item[0]) + eval(item[1]))
            measure = item[ind]
            desc += measure
            name = item[ind+1:]

            self.addItem(Item(name, amount, measure))

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, o):
        if type(o) is not list:
            raise TypeError(f'{type(o)} should be list')
        self._items = o

    @property
    def NumItems(self):
        return len(self._items)

    def addItem(self, o):
        if type(o) is not Item:
            raise TypeError(f'{type(o)} should be item')
        self._items.append(o)

    @property
    def Name(self):
        return self._name

    @Name.setter
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

    @Name.setter
    def Name(self, o):
        if type(o) is not str:
            raise TypeError(f'{type(o)} should be str')
        self._name = o

    @Amount.setter
    def Amount(self, o):
        if type(o) is not float:
            raise TypeError(f'{type(o)} should be float')
        self._amount = o
    
    @Measure.setter
    def Measure(self, o):
        if type(o) is not str:
            raise TypeError(f'{type(o)} should be str')
        self._measure = o

    def __repr__(self):
        s = 'Item<('
        for i in self.__dict__.items():
            s += f'{i[0]}="{i[1]}", '
        s += ')>'
        return s
