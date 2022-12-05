import math
import string

# Read the files for the Input
with open('./Day-05.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Separate the stacks and instruction
data = bulk.split('\n\n')
# print('data : ', data)

# Stacks Informations
stacksBulk = data[0].split('\n')
print('\nstacksBulk : ', stacksBulk)

# Instruction Informations
instructions = data[1].split('\n')
print('\ninstructions : ', instructions)

# Process the Stack information
# Get the positions of each stacks based on the position of the StackNumber information
# The StackNumber information is located on the last line
stackNumbersBulk = stacksBulk[len(stacksBulk) - 1]
stackNumbers = [int(s) for s in stackNumbersBulk.split() if s.isdigit()]
print('\nstackNumbers : ', stackNumbers)


# Get the Stacks data
# Note :
# Ignore the last line because it is only for the StackNumber information
stacks = {}
for stackNumber in stackNumbers:
    stackName = 'stack-' + str(stackNumber)
    stacks[stackName] = []

    # Get the index of the stackNumber
    indexOfStackNumber = stackNumbersBulk.index(str(stackNumber))
    print('indexOfStackNumber : ', indexOfStackNumber)

    cratesBulk = stacksBulk[0:len(stacksBulk)-1]

    # Only get the non-empty values of the crates
    stacks[stackName] = [crates[indexOfStackNumber]
                         for crates in cratesBulk if crates[indexOfStackNumber] != ' ']

    # Currently the Top crates is always on the front of the list
    # We need to make the Top crates always on the back of the list
    stacks[stackName].reverse()

print('\nstacks : ', stacks, '\n')

# Get all instructions
# Each instruction's format :
# number[0] = number of item to move
# number[1] = data to get from
# number[2] = destination of moving the data
for instructionData in instructions:
    instruction = [int(s) for s in instructionData.split() if s.isdigit()]

    # Process the moving using the giant cargo crane
    numberOfItemToMove = instruction[0]
    origin = instruction[1]
    originStack = 'stack-' + str(origin)
    destination = instruction[2]
    destinationStack = 'stack-' + str(destination)

    # Items to move
    originStacks = stacks[originStack]
    lastIndexForMovedItems = len(originStacks)
    firstIndexForMovedItems = lastIndexForMovedItems - numberOfItemToMove
    items = originStacks[firstIndexForMovedItems:lastIndexForMovedItems]
    # print('originStacks : ', originStacks)
    # print('lastIndexForMovedItems : ', lastIndexForMovedItems)
    # print('firstIndexForMovedItems : ', firstIndexForMovedItems)

    # Visually, the items is moved one by one per item
    # So it means we will order of the items will be reversed
    items.reverse()
    print('items to move  : ', items)

    # Add the data to the destination
    stacks[destinationStack].extend(items)

    # Remove the data from the origin
    stacks[originStack] = stacks[originStack][0: firstIndexForMovedItems]

    # Stacks after updates
    print('current Stack  : ', stacks, '\n')

# Get all the top crates
# Currently, all the top crates has been placed on the back of the list
topCrates = [stacks[stack][-1] for stack in stacks]

print('\n============\n')
print('topCrates  : ', ('').join(topCrates))
print('\n============\n')
