# Read the files for the Input
with open('./Day-09.input.txt') as f:
    bulk = f.read()
    # print(bulk)

commands = bulk.split('\n')

initialPosition = {"x": 0, "y": 0}


def coordinateStr(coordinate: dict):
    return ','.join([str(item) for item in coordinate.values()])


# Function for checking the Stepping process
def steppingProcess(direction: str, numberOfSteps: int, inputKnots: list, inputSteppedByTail: list):
    knots = inputKnots.copy()
    numberOfStepsTail = [0 for knot in knots]
    steppedByTail = inputSteppedByTail.copy()

    prevHead = [{"x": knot['x'], "y": knot['y']} for knot in knots]

    print('\n==================\n')
    print('direction : ', direction)
    print('numberOfSteps : ', numberOfSteps)

    # Notes :
    # If the direction is UP, it means the Y is -1
    # If the direction is DOWN, it means the Y is +1
    # If the direction is LEFT, it means the X is -1
    # If the direction is RIGHT, it means the X is +1

    for step in range(0, numberOfSteps):
        for index, knot in enumerate(knots):

            if (index == 0):
                pass
            else:
                head = knots[index-1]
                tail = knots[index]
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
                    tail['x'] = prevHead[index-1]['x']
                    tail['y'] = prevHead[index-1]['y']
                    numberOfStepsTail[index] += 1
                    steppedByTail[index].append(coordinateStr(tail))

                print('head : ', head)
                print('tail : ', tail)
                prevHead[index-1]['x'] = head['x']
                prevHead[index-1]['y'] = head['y']

    result = {
        'numberOfStepsTail': numberOfStepsTail,
        'steppedByTail': steppedByTail,
        'knots': knots
    }

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

    result = steppingProcess(direction, numberOfSteps, knots, knotsStepped)
    knots = result['knots']
    knotsStepped = result['steppedByTail']
    print('result : ', result)


lastKnotSteppedUnique = set(knotsStepped[-1])
print('\n==================\n')
print('lastKnotSteppedUnique : ', len(lastKnotSteppedUnique))
print('\n==================\n')
