#!/usr/bin/python3
from food import *

url = 'https://www.thewholesomedish.com/the-best-classic-chili/'

r = Recipe('the-best-chili', url)

print(r.Items)
