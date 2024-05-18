# Building the meal planner and budget tracker in Excel

# Create weekly meal plan structure
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
meal_types = ["Breakfast", "Lunch", "Dinner"]
# Breakfast is always an egg sandwich, and Lunch is always the same meal prepped on Sunday
breakfast_meal = ["Egg Sandwich"] * 7
lunch_meal = ["Meal Prep"] * 7
# Example dinner meals that rotate
dinner_meals = ["Dinner A", "Dinner B", "Dinner C", "Dinner A", "Dinner B", "Dinner C", "Dinner A"]  # Simplified for one week

# Creating DataFrames
meal_plan_df = pd.DataFrame({
    "Day": days_of_week,
    "Breakfast": breakfast_meal,
    "Lunch": lunch_meal,
    "Dinner": dinner_meals
})

# Create shopping list generator (example based on one week of dinners)
shopping_list = {
    "Ingredient": ["Chicken", "Rice", "Beans", "Beef", "Potatoes", "Carrots", "Fish", "Lettuce", "Tomatoes"],
    "Quantity": [2, 5, 2, 3, 5, 3, 2, 2, 3],
    "Estimated Price": [10, 1, 1, 12, 0.5, 0.75, 15, 1.25, 0.85]
}
shopping_list_df = pd.DataFrame(shopping_list)

# Cost tracker (example placeholders)
cost_tracker = {
    "Item": ["Chicken", "Rice", "Beans"],
    "Quantity": [2, 5, 2],
    "Price per Unit": [5, 1, 0.5],
    "Total Cost": [10, 5, 1]
}
cost_tracker_df = pd.DataFrame(cost_tracker)

# Save to Excel with multiple sheets
with pd.ExcelWriter("/mnt/data/Meal_Planner_and_Budget_Tracker.xlsx") as writer:
    meal_plan_df.to_excel(writer, sheet_name='Weekly Meal Plan', index=False)
    shopping_list_df.to_excel(writer, sheet_name='Shopping List', index=False)
    cost_tracker_df.to_excel(writer, sheet_name='Cost Tracker', index=False)

#"/mnt/data/Meal_Planner_and_Budget_Tracker.xlsx"
