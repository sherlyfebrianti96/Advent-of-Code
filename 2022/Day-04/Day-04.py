import math
import string

# Read the files for the Input
with open('./Day-04.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Separate each pairs
pairs = bulk.split('\n')


totalOfAssignmentFullyContained = 0

totalOfAssignmentOverlapped = 0

# Separate section assignments for each pair
for pair in pairs:
    # This assignmentIds should contains array of 2 unique ID
    assignmentIds = pair.split(',')

    assignment1Ranges = [int(x) for x in assignmentIds[0].split("-")]
    assignment2Ranges = [int(x) for x in assignmentIds[1].split("-")]

    print('\nassignmentRanges : ', assignment1Ranges)
    print('assignmentRanges : ', assignment2Ranges)

    # The `range` needs to have +1 to preserve the last value (end of range)
    assignment1 = range(assignment1Ranges[0], assignment1Ranges[1] + 1)
    assignment2 = range(assignment2Ranges[0], assignment2Ranges[1] + 1)

    print('assignment1 : ', assignment1)
    print('assignment2 : ', assignment2)

    # Find how many assignment pairs does one range fully contain the other
    ass1ContainedByAss2 = assignment1Ranges[0] >= assignment2Ranges[
        0] and assignment1Ranges[1] <= assignment2Ranges[1]

    ass2ContainedByAss1 = assignment2Ranges[0] >= assignment1Ranges[
        0] and assignment2Ranges[1] <= assignment1Ranges[1]

    if (ass1ContainedByAss2 or ass2ContainedByAss1):
        totalOfAssignmentFullyContained += 1
        print('Fully Contained : True')

    #  Part 2
    #  Find how many assignment pairs do the ranges overlap?
    ass1OverlapWithAss2 = assignment2Ranges[0] in assignment1 or assignment2Ranges[1] in assignment1

    ass2OverlapWithAss1 = assignment1Ranges[0] in assignment2 or assignment1Ranges[1] in assignment2

    if (ass1OverlapWithAss2 or ass2OverlapWithAss1):
        totalOfAssignmentOverlapped += 1
        print('Overlap : True')

print('\ntotalOfAssignmentFullyContained : ',
      totalOfAssignmentFullyContained, '\n')

print('\ntotalOfAssignmentOverlapped : ', totalOfAssignmentOverlapped, '\n')
