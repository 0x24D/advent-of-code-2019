#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    with open('../inputs/day3.txt', 'r') as inputFile:
        firstWirePath = inputFile.readline().split(',')
        secondWirePath = inputFile.readline().split(',')

    firstWire = [(0,0)]
    for i in firstWirePath:
        direction = i[0:1]
        distance = int(i[1:]) + 1
        if direction == 'U':
            for y in range(firstWire[-1][1], firstWire[-1][1] + distance):
                firstWire.append((firstWire[-1][0], y))
        elif direction == 'D':
            for y in range(firstWire[-1][1], firstWire[-1][1] - distance, -1):
                firstWire.append((firstWire[-1][0], y))
        elif direction == 'L':
            for x in range(firstWire[-1][0], firstWire[-1][0] - distance, -1):
                firstWire.append((x, firstWire[-1][1]))
        else:
            for x in range(firstWire[-1][0], firstWire[-1][0] + distance):
                firstWire.append((x, firstWire[-1][1]))

    secondWire = [(0,0)]
    for i in secondWirePath:
        direction = i[0:1]
        distance = int(i[1:]) + 1
        if direction == 'U':
            for y in range(secondWire[-1][1], secondWire[-1][1] + distance):
                secondWire.append((secondWire[-1][0], y))
        elif direction == 'D':
            for y in range(secondWire[-1][1], secondWire[-1][1] - distance, -1):
                secondWire.append((secondWire[-1][0], y))
        elif direction == 'L':
            for x in range(secondWire[-1][0], secondWire[-1][0] - distance, -1):
                secondWire.append((x, secondWire[-1][1]))
        else:
            for x in range(secondWire[-1][0], secondWire[-1][0] + distance):
                secondWire.append((x, secondWire[-1][1]))

    intersections = list(set(firstWire) & set(secondWire))
    distances = []
    for i in intersections:
        if i != (0,0):
            distances.append((abs(0 - i[0])) + (abs(0 - i[1])))
    print('Manhattan distance to closest intersection is: {}'.format(min(distances)))

