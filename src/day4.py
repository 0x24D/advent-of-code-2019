#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    puzzleInput = "278384-824795"
    passwordRange = list(map(int, puzzleInput.split('-')))

    notDecreasing = []
    for i in range(passwordRange[0], passwordRange[1] + 1):
        increasing = True
        for n in range(1, 6):
            if str(i)[n - 1] > str(i)[n]:
                increasing = False
                break
        if increasing:
            notDecreasing.append(i)

    duplicateNumbers = []
    for i in notDecreasing:
        for n in range(1, 6):
            if str(i)[n - 1] == str(i)[n]:
                duplicateNumbers.append(i)
                break
    print("Number of different passwords in range: {}".format(len(duplicateNumbers)))

    # Part 2
    doubleNumbers = []
    for i in duplicateNumbers:
        numDuplicates = 0
        numDoubles = 0
        for n in range(1, 6):
            if str(i)[n - 1] == str(i)[n]:
                numDuplicates += 1
            else:
                if numDuplicates == 1:
                    numDoubles += 1
                else:
                    numDuplicates = 0
        if str(i)[-1] == str(i)[-2]:
            numDuplicates += 1
        if numDuplicates == 2:
            numDoubles += 1
        if numDoubles != 0:
            doubleNumbers.append(i)
    print("Number of different passwords in range: {}".format(len(doubleNumbers)))
