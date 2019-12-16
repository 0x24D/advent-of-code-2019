#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    intCodeStr = ''
    with open('../inputs/day2.txt', 'r') as inputFile:
        intCodeStr = inputFile.read()
    intCodeArr = list(map(int, intCodeStr.split(',')))
    skipTo = -1
    intCodeArr[1] = 12
    intCodeArr[2] = 2
    for i, code in enumerate(intCodeArr):
        if skipTo != -1 and i != skipTo:
            pass
        else:
            if code == 1:
                intCodeArr[intCodeArr[i + 3]] = intCodeArr[intCodeArr[i + 1]] + intCodeArr[intCodeArr[i + 2]]
                skipTo = i + 4
            elif code == 2:
                intCodeArr[intCodeArr[i + 3]] = intCodeArr[intCodeArr[i + 1]] * intCodeArr[intCodeArr[i + 2]]
                skipTo = i + 4
            elif code == 99:
                break
            else:
                print("Something went wrong exiting")
                exit(1)
    print('Value at position 0:', intCodeArr[0])

    # Part 2
    intCodeStr = ''
    with open('../inputs/day2.txt', 'r') as inputFile:
        intCodeStr = inputFile.read()
    for noun in range(99):
        for verb in range(99):
            intCodeArr = list(map(int, intCodeStr.split(',')))
            skipTo = -1
            intCodeArr[1] = noun
            intCodeArr[2] = verb
            for i, code in enumerate(intCodeArr):
                if skipTo != -1 and i != skipTo:
                    pass
                else:
                    if code == 1:
                        intCodeArr[intCodeArr[i + 3]] = intCodeArr[intCodeArr[i + 1]] + intCodeArr[intCodeArr[i + 2]]
                        skipTo = i + 4
                    elif code == 2:
                        intCodeArr[intCodeArr[i + 3]] = intCodeArr[intCodeArr[i + 1]] * intCodeArr[intCodeArr[i + 2]]
                        skipTo = i + 4
                    elif code == 99:
                        break
                    else:
                        print("Something went wrong exiting")
                        exit(1)
            if (intCodeArr[0] == 19690720):
                print('Answer:', 100 * noun + verb)
                break
