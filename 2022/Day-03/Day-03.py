import math
import string

# Read the files for the Input
with open('./Day-03.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Separate each rucksacks
rucksacks = bulk.split('\n')


# Define the priorities
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
#
# In this case, `string.ascii_letters` will return all alphabets
# with order a-z and A-Z
priorities = list(string.ascii_letters)

totalOfPriorities = 0

for rucksack in rucksacks:
    numberOfCompartment = 2
    numberOfItemsInRucksack = len(rucksack)
    itemsPerCompartment = math.floor(
        numberOfItemsInRucksack/numberOfCompartment)

    print('-------\n')

    # Separate the items for each compartments
    compartment1 = rucksack[0:itemsPerCompartment]
    compartment2 = rucksack[itemsPerCompartment:numberOfItemsInRucksack]

    itemType = ''

    # Check which one is appearing in both compartments
    for item in compartment1:
        if item in compartment2:
            itemType = item

    # Get the priority of this rucksack's item type
    rucksackPriority = priorities.index(itemType) + 1

    print('itemType : ', itemType, '\n')
    print('rucksackPriority : ', rucksackPriority, '\n')

    # Add the rucksack's priority to the total
    totalOfPriorities += rucksackPriority

print('\n============\n')
print('Total of the priorities : ', totalOfPriorities)
print('\n============\n')
