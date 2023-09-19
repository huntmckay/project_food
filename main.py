from recipe_scrapers import scrape_me
from quantulum3 import parser

s = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

unfiltered = s.ingredients()

def filter(a):
    filtered = {}
    for i in a:
        quant = parser.parse(i)
        print(quant)
print(filter(unfiltered))
