import json

# Ingredient costs dictionary
ingredient_costs = {
    'flour': 2.5,  # per kg
    'sugar': 1.5,  # per kg
    'butter': 3.0,  # per kg
    'milk': 0.8,  # per liter
    'eggs': 0.2,  # per egg
    'baking_powder': 0.02,  # per gram
    'baking_soda': 0.015,  # per gram,
    'vanilla_extract': 20.0,  # per liter,
    'cinnamon': 0.03,  # per gram,
    'raisins': 5.0,  # per kg
    'water': 0.01,  # per liter
    'yeast': 0.05,  # per oz
    'salt': 1  # per kg
}

# Write ingredient costs to JSON file
with open("ingredient_costs.json", "w") as ingredient_cost_file:
    ingredient_cost_file.write(json.dumps(ingredient_costs))

# Read the JSON file
with open("ingredient_costs.json", "r") as json_file:
    ingredient_costs = json.load(json_file)

# Convert the JSON to CSV
# Open data.csv in append mode
with open("data.csv", "a") as data_csv:
    # Loop over the ingredient costs dictionary
    for ingredient_name, amount in ingredient_costs.items():
        # Make the ingredient and amount become a string, like this: flour,2.5
        ingredient_string = "\n" + ingredient_name + "," + str(amount)
        # Append the string to the end of the CSV file
        data_csv.write(ingredient_string)

print("JSON to CSV conversion completed and appended to data.csv.")

# Verify the contents of data.csv
print("Contents of data.csv:")
with open("data.csv", "r") as data_csv:
    for line in data_csv:
        print(line.strip())
