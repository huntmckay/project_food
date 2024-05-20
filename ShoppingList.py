import yaml

class ShoppingList:
    def __init__(self, filename):
        self.filename = filename
        self.shopping_list = []
        self.recipes = []

    def load(self):
        with open(self.filename, 'r') as f:
            self.shopping_list = yaml.load(f)

    def save(self):
        with open(self.filename, 'w') as f:
            yaml.dump(self.shopping_list, f)

    def add(self, item):
        self.shopping_list.append(item)

    def remove(self, item):
        self.shopping_list.remove(item)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def __str__(self):
        return str(self.shopping_list)


# This should collect all the items from the recipes listed in the recipe path
# and add them to the shopping list
working_dir = 'C:\Users\HsMck\OneDrive\code\project_food'
recipe_path = 'C:\Users\HsMck\OneDrive\code\project_food\week_one_recipes'

shopping_list = ShoppingList('shopping_list.yaml')
shopping_list.load()
