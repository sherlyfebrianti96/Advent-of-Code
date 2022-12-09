# Read the files for the Input
with open('./Day-09.input.txt') as f:
    bulk = f.read()
    # print(bulk)

commands = bulk.split('\n')

initialX = {"x": 0, "y": 0}
prevHead = {"x": 0, "y": 0}
head = {"x": 0, "y": 0}
tail = {"x": 0, "y": 0}


def coordinateStr(coordinate: dict):
    return ','.join([str(item) for item in coordinate.values()])


numberOfStepsTail = 0

steppedByTail = [coordinateStr(tail)]

for command in commands:
    data = command.split(' ')

    direction = data[0]
    numberOfSteps = int(data[1])

    print('\n==================\n')
    print('direction : ', direction)
    print('numberOfSteps : ', numberOfSteps)

    # Notes :
    # If the direction is UP, it means the Y is -1
    # If the direction is DOWN, it means the Y is +1
    # If the direction is LEFT, it means the X is -1
    # If the direction is RIGHT, it means the X is +1

    match direction:
        case 'U':
            for step in range(0, numberOfSteps):
                print('\n--------------\n')
                print("UP :")
                head["y"] -= 1

                # Check if the Head and Tail position is side-by-side
                # If it is not side-by-side, we need to make the tail take over the last position of the head
                distanceX = abs(head["x"] - tail["x"])
                distanceY = abs(head["y"] - tail["y"])
                if (distanceX > 1 or distanceY > 1):
                    tail['x'] = prevHead['x']
                    tail['y'] = prevHead['y']
                    numberOfStepsTail += 1
                    steppedByTail.append(coordinateStr(tail))

                print('head : ', head)
                print('tail : ', tail)
                prevHead['x'] = head['x']
                prevHead['y'] = head['y']
            pass
        case 'D':
            for step in range(0, numberOfSteps):
                print('\n--------------\n')
                print("DOWN :")
                head["y"] += 1

                # Check if the Head and Tail position is side-by-side
                # If it is not side-by-side, we need to make the tail take over the last position of the head
                distanceX = abs(head["x"] - tail["x"])
                distanceY = abs(head["y"] - tail["y"])
                if (distanceX > 1 or distanceY > 1):
                    tail['x'] = prevHead['x']
                    tail['y'] = prevHead['y']
                    numberOfStepsTail += 1
                    steppedByTail.append(coordinateStr(tail))

                print('head : ', head)
                print('tail : ', tail)
                prevHead['x'] = head['x']
                prevHead['y'] = head['y']
            pass
        case 'L':
            for step in range(0, numberOfSteps):
                print('\n--------------\n')
                print("LEFT :")
                head["x"] -= 1

                # Check if the Head and Tail position is side-by-side
                # If it is not side-by-side, we need to make the tail take over the last position of the head
                distanceX = abs(head["x"] - tail["x"])
                distanceY = abs(head["y"] - tail["y"])
                if (distanceX > 1 or distanceY > 1):
                    tail['x'] = prevHead['x']
                    tail['y'] = prevHead['y']
                    numberOfStepsTail += 1
                    steppedByTail.append(coordinateStr(tail))

                print('head : ', head)
                print('tail : ', tail)
                prevHead['x'] = head['x']
                prevHead['y'] = head['y']
            pass
        case 'R':
            for step in range(0, numberOfSteps):
                print('\n--------------\n')
                print("RIGHT :")
                head["x"] += 1

                # Check if the Head and Tail position is side-by-side
                # If it is not side-by-side, we need to make the tail take over the last position of the head
                distanceX = abs(head["x"] - tail["x"])
                distanceY = abs(head["y"] - tail["y"])
                if (distanceX > 1 or distanceY > 1):
                    tail['x'] = prevHead['x']
                    tail['y'] = prevHead['y']
                    numberOfStepsTail += 1
                    steppedByTail.append(coordinateStr(tail))

                print('head : ', head)
                print('tail : ', tail)
                prevHead['x'] = head['x']
                prevHead['y'] = head['y']
            pass
        case other:
            # Do nothing
            pass

print('steppedByTail : ', steppedByTail)
steppedByTailUnique = set(steppedByTail)

print('\n==================\n')
print('numberOfStepsTail : ', numberOfStepsTail)
print('\n==================\n')
print('steppedByTailUnique : ', len(steppedByTailUnique))
print('\n==================\n')
