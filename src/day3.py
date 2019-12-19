#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    with open('../inputs/day3.txt', 'r') as inputFile:
        firstWirePath = inputFile.readline().split(',')
        secondWirePath = inputFile.readline().split(',')

    firstWire = [(0,0)]
    for i in firstWirePath:
        direction = i[0:1]
        distance = int(i[1:])
        currentX = firstWire[-1][0]
        currentY = firstWire[-1][1]
        if direction == 'U':
            for y in range(currentY + 1, currentY + 1  + distance):
                firstWire.append((currentX, y))
        elif direction == 'D':
            for y in range(currentY - 1, currentY - 1 - distance, -1):
                firstWire.append((currentX, y))
        elif direction == 'L':
            for x in range(currentX - 1, currentX - 1 - distance, -1):
                firstWire.append((x, currentY))
        else:
            for x in range(currentX + 1, currentX + 1 + distance):
                firstWire.append((x, currentY))

    secondWire = [(0,0)]
    for i in secondWirePath:
        direction = i[0:1]
        distance = int(i[1:])
        currentX = secondWire[-1][0]
        currentY = secondWire[-1][1]
        if direction == 'U':
            for y in range(currentY + 1, currentY + 1  + distance):
                secondWire.append((currentX, y))
        elif direction == 'D':
            for y in range(currentY - 1, currentY - 1 - distance, -1):
                secondWire.append((currentX, y))
        elif direction == 'L':
            for x in range(currentX - 1, currentX - 1 - distance, -1):
                secondWire.append((x, currentY))
        else:
            for x in range(currentX + 1, currentX + 1 + distance):
                secondWire.append((x, currentY))

    intersections = list(set(firstWire) & set(secondWire))
    intersections.remove((0, 0))
    distances = []
    for i in intersections:
        distances.append((abs(0 - i[0])) + (abs(0 - i[1])))
    print('Manhattan distance to closest intersection is: {}'.format(min(distances)))

    # Part 2
    steps = []
    for i in intersections:
        steps.append(firstWire.index(i) + secondWire.index(i))
    print('Fewest combined steps to reach an intersection is: {}'.format(min(steps)))

