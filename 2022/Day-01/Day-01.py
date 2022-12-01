# bulk = input("Enter the foods carried by the Elves : ");

# Read the files for the Input
with open('./Day-01.input.txt') as f:
    bulk = f.read()
    print(bulk)

# Separate the inventories of each Elves
inventories = bulk.split('\n\n')

totalCaloriesArr = []

# Check the inventories one by one
for inventory in inventories:
    # Calories still in String format from the input
    caloriesStr = inventory.split('\n')

    # Convert the Calories to integer
    calories = list(map(int, caloriesStr))

    totalCalories = sum(calories)
    totalCaloriesArr.append(totalCalories)
    print('calories : ', calories, ' = ', totalCalories, '\n')

# Get the biggest Calories
largestCalories = max(totalCaloriesArr)
print('Largest Calories : ', largestCalories, '\n')
