# Read the files for the Input
with open('./Day-08.input.txt') as f:
    bulk = f.read()
    # print(bulk)

visibleTrees = 0
highestScenicScore = 0

coveredX = []
coveredY = []

# The forest is 2D
# Distinguish between the trees that is covered and not visible
rows = bulk.split('\n')
for rowIndex, row in enumerate(rows):
    for treeIndex, tree in enumerate(row):
        # Find the Outer part of the forest
        isOuterTop = rowIndex == 0
        isOuterLeft = treeIndex == 0
        isOuterRight = treeIndex == len(row) - 1
        isOuterBottom = rowIndex == len(rows) - 1

        isOuterPart = isOuterTop or isOuterLeft or isOuterRight or isOuterBottom

        if isOuterPart:
            visibleTrees += 1
        else:
            pass
            # Check if the current tree is covered by the surrounding trees
            # It means we need to check if the surounding tress around the current trees is higher than current trees
            topLeft = rows[rowIndex-1][treeIndex-1]
            topMiddle = rows[rowIndex-1][treeIndex]
            topRight = rows[rowIndex-1][treeIndex+1]
            middleLeft = rows[rowIndex][treeIndex-1]
            # current = rows[rowIndex][treeIndex] # This value equals `tree` value
            middleRight = rows[rowIndex][treeIndex+1]
            bottomLeft = rows[rowIndex+1][treeIndex-1]
            bottomMiddle = rows[rowIndex+1][treeIndex]
            bottomRight = rows[rowIndex+1][treeIndex+1]

            # surroundingTrees = [topLeft, topMiddle, topRight, middleLeft,
            #                     middleRight, bottomLeft, bottomMiddle, bottomRight]

            # Part 1
            # The surrounding Trees is only checked based on current Tree's top, left, right, bottom
            # It will not checking the edge of it
            currentXIndexPosition = treeIndex + 1
            currentYIndexPosition = rowIndex + 1

            numberOfItemInTopRow = currentYIndexPosition - 1
            numberOfItemInLeftRow = currentXIndexPosition - 1
            numberOfItemInRightRow = len(row) - currentXIndexPosition
            numberOfItemInRBottomRow = len(rows) - numberOfItemInTopRow

            surroundingTopTrees = [rows[index][currentXIndexPosition - 1]
                                   for index in range(0, numberOfItemInTopRow)]

            surroundingLeftTrees = list(row[0:(numberOfItemInLeftRow)])

            surroundingRightTrees = list(row[currentXIndexPosition:(
                currentXIndexPosition+numberOfItemInRightRow)])

            surroundingBottomTrees = [rows[numberOfItemInTopRow + index]
                                      [currentXIndexPosition-1] for index in range(1, numberOfItemInRBottomRow)]

            coveredBySurroundingTop = any(
                item >= tree for item in surroundingTopTrees)
            coveredBySurroundingLeft = any(
                item >= tree for item in surroundingLeftTrees)
            coveredBySurroundingRight = any(
                item >= tree for item in surroundingRightTrees)
            coveredBySurroundingBottom = any(
                item >= tree for item in surroundingBottomTrees)

            if (coveredBySurroundingTop and coveredBySurroundingLeft and coveredBySurroundingRight and coveredBySurroundingBottom):
                pass
            else:
                visibleTrees += 1

            # Part 2
            # Highest scenic score
            # It means they want to find the view that can see trees as much as possible
            numberOfTreesVisibleTop = 0
            numberOfTreesVisibleLeft = 0
            numberOfTreesVisibleRight = 0
            numberOfTreesVisibleBottom = 0

            # numberOfTreesVisibleTop = [
            #     item for item in surroundingTopTrees if item <= tree]
            # numberOfTreesVisibleLeft = [
            #     item for item in surroundingLeftTrees if item <= tree]
            # numberOfTreesVisibleRight = [
            #     item for item in surroundingRightTrees if item <= tree]
            # numberOfTreesVisibleBottom = [
            #     item for item in surroundingBottomTrees if item <= tree]

            # numberOfTreesVisibleTop
            # Reverse the SurroundingTopTrees
            # So we can check it from the tree nearest to our current tree
            surroundingTopTrees.reverse()
            for item in surroundingTopTrees:
                numberOfTreesVisibleTop += 1

                if item >= tree:
                    # If the current tree is higher than our current tree,
                    # it means it is blocking the rest of trees from us
                    break

            # numberOfTreesVisibleLeft
            # Reverse the surroundingLeftTrees
            # So we can check it from the tree nearest to our current tree
            surroundingLeftTrees.reverse()
            for item in surroundingLeftTrees:
                numberOfTreesVisibleLeft += 1

                if item >= tree:
                    # If the current tree is higher than our current tree,
                    # it means it is blocking the rest of trees from us
                    break

            # numberOfTreesVisibleRight
            for item in surroundingRightTrees:
                numberOfTreesVisibleRight += 1

                if item >= tree:
                    # If the current tree is higher than our current tree,
                    # it means it is blocking the rest of trees from us
                    break

            # numberOfTreesVisibleBottom
            for item in surroundingBottomTrees:
                numberOfTreesVisibleBottom += 1

                if item >= tree:
                    # If the current tree is higher than our current tree,
                    # it means it is blocking the rest of trees from us
                    break

            scenicScore = numberOfTreesVisibleTop * numberOfTreesVisibleLeft * \
                numberOfTreesVisibleRight * numberOfTreesVisibleBottom

            if (scenicScore > highestScenicScore):
                highestScenicScore = scenicScore


print('\n============\n')
print('visibleTrees : ', visibleTrees)
print('\n============\n')
print('highestScenicScore : ', highestScenicScore)
print('\n============\n')
