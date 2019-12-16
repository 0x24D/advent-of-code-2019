#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    total = 0
    with open('../inputs/day1.txt', 'r') as inputFile:
        for c, line in enumerate(inputFile):
            total += (int(line) // 3) - 2
    print('Total fuel required is:', total)

    # Part 2
    total = 0
    with open('../inputs/day1.txt', 'r') as inputFile:
        for c, line in enumerate(inputFile):
            fuelRequired = (int(line) // 3) - 2
            while fuelRequired > 0:
                total += fuelRequired
                fuelRequired = (fuelRequired // 3) - 2
    print('Actual total fuel required is:', total)

