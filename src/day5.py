#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    with open('../inputs/day5.txt', 'r') as inputFile:
        intCodeStr = inputFile.read()
    intCodeArr = list(map(int, intCodeStr.split(',')))
    skipTo = 0
    inputBuffer = 1
    outputBuffer = 0
    for i, c in enumerate(intCodeArr):
        if i != skipTo:
            pass
        else:
            opcode = int(str(c)[-2:])
            try:
                firstParamMode = int(str(c)[-3])
            except IndexError:
                firstParamMode = 0
            try:
                secondParamMode = int(str(c)[-4])
            except IndexError:
                secondParamMode = 0
            try:
                thirdParamMode = int(str(c)[-5])
            except IndexError:
                thirdParamMode = 0
            if opcode == 1:
                intCodeArr[intCodeArr[i + 3]] = (intCodeArr[intCodeArr[i + 1]] if firstParamMode == 0 else intCodeArr[i + 1]) + (
                    intCodeArr[intCodeArr[i + 2]] if secondParamMode == 0 else intCodeArr[i + 2])
                skipTo = i + 4
            elif opcode == 2:
                intCodeArr[intCodeArr[i + 3]] = (intCodeArr[intCodeArr[i + 1]] if firstParamMode == 0 else intCodeArr[i + 1]) * (
                    intCodeArr[intCodeArr[i + 2]] if secondParamMode == 0 else intCodeArr[i + 2])
                skipTo = i + 4
            elif opcode == 3:
                if firstParamMode == 0:
                    intCodeArr[intCodeArr[i + 1]] = inputBuffer
                else:
                    intCodeArr[i + 1] = inputBuffer
                skipTo = i + 2
            elif opcode == 4:
                outputBuffer = intCodeArr[intCodeArr[i + 1]
                                          ] if firstParamMode == 0 else intCodeArr[i + 1]
                skipTo = i + 2
                print('Output for system ID 1: {}'.format(outputBuffer))
            elif opcode == 99:
                break
            else:
                print('Something went wrong, exiting')
                exit(1)

    # Part 2
    intCodeArr = list(map(int, intCodeStr.split(',')))
    skipTo = 0
    inputBuffer = 5
    outputBuffer = 0
    for i, c in enumerate(intCodeArr):
        if i != skipTo:
            pass
        else:
            opcode = int(str(c)[-2:])
            try:
                firstParamMode = int(str(c)[-3])
            except IndexError:
                firstParamMode = 0
            try:
                secondParamMode = int(str(c)[-4])
            except IndexError:
                secondParamMode = 0
            try:
                thirdParamMode = int(str(c)[-5])
            except IndexError:
                thirdParamMode = 0
            if opcode == 1:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                secondVal = intCodeArr[intCodeArr[i + 2]
                                       ] if secondParamMode == 0 else intCodeArr[i + 2]
                intCodeArr[intCodeArr[i + 3]] = firstVal + secondVal
                skipTo = i + 4
            elif opcode == 2:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                secondVal = intCodeArr[intCodeArr[i + 2]
                                       ] if secondParamMode == 0 else intCodeArr[i + 2]
                intCodeArr[intCodeArr[i + 3]] = firstVal * secondVal
                skipTo = i + 4
            elif opcode == 3:
                intCodeArr[intCodeArr[i + 1]] = inputBuffer
                skipTo = i + 2
            elif opcode == 4:
                outputBuffer = intCodeArr[intCodeArr[i + 1]
                                          ] if firstParamMode == 0 else intCodeArr[i + 1]
                print('Diagnostic code for system ID 5: {}'.format(outputBuffer))
                skipTo = i + 2
            elif opcode == 5:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                if firstVal != 0:
                    secondVal = intCodeArr[intCodeArr[i + 2]
                                           ] if secondParamMode == 0 else intCodeArr[i + 2]
                    skipTo = secondVal
                else:
                    skipTo = i + 3
            elif opcode == 6:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                if firstVal == 0:
                    secondVal = intCodeArr[intCodeArr[i + 2]
                                           ] if secondParamMode == 0 else intCodeArr[i + 2]
                    skipTo = secondVal
                else:
                    skipTo = i + 3
            elif opcode == 7:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                secondVal = intCodeArr[intCodeArr[i + 2]
                                       ] if secondParamMode == 0 else intCodeArr[i + 2]
                intCodeArr[intCodeArr[i + 3]
                           ] = 1 if firstVal < secondVal else 0
                skipTo = i + 4
            elif opcode == 8:
                firstVal = intCodeArr[intCodeArr[i + 1]
                                      ] if firstParamMode == 0 else intCodeArr[i + 1]
                secondVal = intCodeArr[intCodeArr[i + 2]
                                       ] if secondParamMode == 0 else intCodeArr[i + 2]
                intCodeArr[intCodeArr[i + 3]
                           ] = 1 if firstVal == secondVal else 0
                skipTo = i + 4
            elif opcode == 99:
                break
            else:
                print('Something went wrong, exiting')
                exit(1)
