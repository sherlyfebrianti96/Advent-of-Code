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

    for step in range(0, numberOfSteps):
        match direction:
            case 'U':
                print('\n--------------\n')
                print("UP :")
                head["y"] -= 1
            case 'D':
                print('\n--------------\n')
                print("DOWN :")
                head["y"] += 1
            case 'L':
                print('\n--------------\n')
                print("LEFT :")
                head["x"] -= 1
            case 'R':
                print('\n--------------\n')
                print("RIGHT :")
                head["x"] += 1
            case other:
                # Do nothing
                pass

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

    result = {
        'numberOfStepsTail': numberOfStepsTail,
        'steppedByTail': steppedByTail,
        'head': head,
        'tail': tail
    }
    print('\n--------------\n')
    print('result : ', result)

    return result


numberOfKnots = 2

knots = [{"x": 0, "y": 0} for i in range(0, numberOfKnots)]
knotsStepped = [[coordinateStr(knot)] for knot in knots]
print('knots : ', knots)
print('knotsStepped : ', knotsStepped)

for command in commands:
    data = command.split(' ')

    direction = data[0]
    numberOfSteps = int(data[1])

    for index, knot in enumerate(knots):
        if (index == 0):
            pass
        else:
            result = steppingProcess(
                direction, numberOfSteps, knots[index - 1], knot)

            # Update the Knots data
            knots[index-1] = result['head']
            knots[index] = result['tail']
            knotsStepped[index] += result['steppedByTail']


lastKnotSteppedUnique = set(knotsStepped[-1])
print('\n==================\n')
print('lastKnotSteppedUnique : ', len(lastKnotSteppedUnique))
print('\n==================\n')
