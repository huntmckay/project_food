import yaml

food_prices_file_path = 'food-prices.yaml'
servings = input('how many servings do you want to make? default is 4')
meal_plan_week = input('which meal plan do you want to use? (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)')
recipe_dir_path = 'recipes'

# Open up food-prices.yaml
with open(food_prices_file_path) as file:
    food_prices = yaml.load(file, Loader=yaml.FullLoader)

# Open up meal plan weeks work of yamls, append to one yaml in mem
meal_plan = []
for i in range(1, 8):
    with open(f'{recipe_dir_path}/week-{meal_plan_week}/day-{i}.yaml') as file:
        meal_plan.append(yaml.load(file, Loader=yaml.FullLoader))
# Calculate total cost of meal plan


# Create Shopping List

# Write Shopping List to file

# Print Shopping List