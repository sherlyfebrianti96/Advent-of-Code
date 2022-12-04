import math
import string

# Read the files for the Input
with open('./Day-04.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Separate each pairs
pairs = bulk.split('\n')


totalOfAssignmentInOneRange = 0

# Separate section assignments for each pair
for pair in pairs:
    # This assignmentIds should contains array of 2 unique ID
    assignmentIds = pair.split(',')

    assignment1Ranges = [int(x) for x in assignmentIds[0].split("-")]
    assignment2Ranges = [int(x) for x in assignmentIds[1].split("-")]

    ass1ContainedByAss2 = assignment1Ranges[0] >= assignment2Ranges[
        0] and assignment1Ranges[1] <= assignment2Ranges[1]

    ass2ContainedByAss1 = assignment2Ranges[0] >= assignment1Ranges[
        0] and assignment2Ranges[1] <= assignment1Ranges[1]
    
    if (ass1ContainedByAss2 or ass2ContainedByAss1):
        totalOfAssignmentInOneRange += 1

print('\ntotalOfAssignmentInOneRange : ', totalOfAssignmentInOneRange, '\n')
