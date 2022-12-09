# Read the files for the Input
with open('./Day-09.input.txt') as f:
    bulk = f.read()
    # print(bulk)

commands = bulk.split('\n')

initialPosition = {"x": 0, "y": 0}


def coordinateStr(coordinate: dict):
    return ','.join([str(item) for item in coordinate.values()])


# Function for checking the Stepping process
def steppingProcess(direction: str, numberOfSteps: int, inputHead: dict, inputTail: dict):
    head = inputHead.copy()
    tail = inputTail.copy()
    numberOfStepsTail = 0
    steppedByTail = []
    prevHead = {"x": head['x'], "y": head['y']}

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

    result = {
        'numberOfStepsTail': numberOfStepsTail,
        'steppedByTail': steppedByTail,
        'head': head,
        'tail': tail
    }
    print('\n--------------\n')
    print('result : ', result)

    return result


knot1 = {"x": 0, "y": 0}
knot2 = {"x": 0, "y": 0}
knot2Stepped = [coordinateStr(knot2)]

for command in commands:
    data = command.split(' ')

    direction = data[0]
    numberOfSteps = int(data[1])

    result = steppingProcess(direction, numberOfSteps, knot1, knot2)

    # Update the Knots data
    knot1 = result['head']
    knot2 = result['tail']
    knot2Stepped += result['steppedByTail']
    print('knot2Stepped : ', knot2Stepped)

knot2SteppedUnique = set(knot2Stepped)
print('\n==================\n')
print('knot2SteppedUnique : ', len(knot2SteppedUnique))
print('\n==================\n')
