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

# Part 2
# Get the top 3 biggest Calories
# and then get the total of those 3 Calories

# Sort the totalCaloriesArr by DESC
totalCaloriesArr.sort(reverse=True)

# Get the total of top 3 biggest Calories
top3BiggestCalories = sum(totalCaloriesArr[0:3])
print('Top 3 biggest Calories : ', top3BiggestCalories, '\n')
