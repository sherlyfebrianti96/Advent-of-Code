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


def getPriorities(compartments):
    compartment1 = compartments[0]
    compartmentN = compartments[1:len(compartments)]

    itemType = ''

    for item in compartment1:
        isItemType = []
        for compartment in compartmentN:
            isItemType.append(item in compartment)

        if False in isItemType:
            pass
        else:
            itemType = item

    # Get the priority of this rucksack's item type
    rucksackPriority = priorities.index(itemType) + 1

    print('itemType : ', itemType, '\n')
    print('rucksackPriority : ', rucksackPriority, '\n')

    return int(rucksackPriority)


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

    totalOfPriorities += getPriorities([compartment1, compartment2])

print('\n============\n')
print('Total of the priorities : ', totalOfPriorities)
print('\n============\n')


# Part 2
# Make the number of priorities become flexible

rucksacks = bulk.split('\n')

totalOfPriorities = 0

numberOfLines = 3

numberOfGroup = int(len(rucksacks) / numberOfLines)

# Separate each group by three lines
for groupIndex in range(numberOfGroup):
    lastIndex = (groupIndex + 1) * numberOfLines
    startingIndex = lastIndex - numberOfLines
    compartments = rucksacks[startingIndex:lastIndex]

    print('-------\n')
    print('compartments : ', compartments)
    totalOfPriorities += getPriorities(compartments)

print('\n============\n')
print('Total of the priorities : ', totalOfPriorities)
print('\n============\n')
