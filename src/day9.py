#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1 and 2
    for inputBuffer in [1, 2]:
        with open('../inputs/day9.txt', 'r') as inputFile:
            intCodeStr = inputFile.read()
        intCodeArr = list(map(int, intCodeStr.split(',')))
        skipTo = 0
        outputBuffer = 0
        base = 0
        relativeBase = 0
        memory = dict()
        while True:
            c = str(intCodeArr[base])
            opcode = int(c[-2:])
            try:
                firstParamMode = int(c[-3])
            except IndexError:
                firstParamMode = 0
            try:
                secondParamMode = int(c[-4])
            except IndexError:
                secondParamMode = 0
            try:
                thirdParamMode = int(c[-5])
            except IndexError:
                thirdParamMode = 0

            try:
                firstParam = intCodeArr[intCodeArr[base + 1]] if firstParamMode == 0 else intCodeArr[base + 1] if firstParamMode == 1 else intCodeArr[relativeBase + intCodeArr[base + 1]] 
            except IndexError:
                try:
                    firstParam = memory[str(intCodeArr[base + 1])] if firstParamMode == 0 else memory[str(base + 1)] if firstParamMode == 1 else memory[str(relativeBase + intCodeArr[base + 1])]
                except (IndexError, KeyError):
                    pass
            try:
                secondParam = intCodeArr[intCodeArr[base + 2]] if secondParamMode == 0 else intCodeArr[base + 2] if secondParamMode == 1 else intCodeArr[relativeBase + intCodeArr[base + 2]]
            except IndexError:
                try:
                    secondParam = memory[str(intCodeArr[base + 2])] if secondParamMode == 0 else memory[str(base + 2)] if secondParamMode == 1 else memory[str(relativeBase + intCodeArr[base + 2])]
                except (IndexError, KeyError):
                    pass
            try:
                thirdParam = intCodeArr[intCodeArr[base + 3]] if thirdParamMode == 0 else intCodeArr[base + 3] if thirdParamMode == 1 else intCodeArr[relativeBase + intCodeArr[base + 3]] 
            except IndexError:
                try:
                    thirdParam = memory[str(intCodeArr[base + 3])] if thirdParamMode == 0 else memory[str(base + 3)] if thirdParamMode == 1 else memory[str(relativeBase + intCodeArr[base + 3])]
                except (IndexError, KeyError):
                    pass
            if opcode == 1:
                b = relativeBase if thirdParamMode == 2 else 0
                if len(intCodeArr) > b + intCodeArr[base + 3]:
                    intCodeArr[b + intCodeArr[base + 3]] = firstParam + secondParam
                else:
                    memory[str(b + intCodeArr[base + 3])] = firstParam + secondParam
                base += 4
            elif opcode == 2:
                b = relativeBase if thirdParamMode == 2 else 0
                if len(intCodeArr) > b + intCodeArr[base + 3]:
                    intCodeArr[b + intCodeArr[base + 3]] = firstParam * secondParam
                else:
                    memory[str(b + intCodeArr[base + 3])] = firstParam * secondParam
                base += 4
            elif opcode == 3:
                b = relativeBase if firstParamMode == 2 else 0
                if len(intCodeArr) > b + intCodeArr[base + 1]:
                    intCodeArr[b + intCodeArr[base + 1]] = inputBuffer
                else:
                    memory[str(b + intCodeArr[base + 1])] = inputBuffer
                base += 2
            elif opcode == 4:
                outputBuffer = firstParam
                print(outputBuffer)
                base += 2
            elif opcode == 5:
                if firstParam != 0:
                    base = secondParam
                else:
                    base += 3
            elif opcode == 6:
                if firstParam == 0:
                    base = secondParam
                else:
                    base += 3
            elif opcode == 7:
                b = relativeBase if thirdParamMode == 2 else 0
                if len(intCodeArr) > b + intCodeArr[base + 3]:
                    intCodeArr[b + intCodeArr[base + 3]] = 1 if firstParam < secondParam else 0
                else:
                    memory[str(b + intCodeArr[base + 3])] = 1 if firstParam < secondParam else 0
                base += 4
            elif opcode == 8:
                b = relativeBase if thirdParamMode == 2 else 0
                if len(intCodeArr) > b + intCodeArr[base + 3]:
                    intCodeArr[b + intCodeArr[base + 3]] = 1 if firstParam == secondParam else 0
                else:
                    memory[str(b + intCodeArr[base + 3])] = 1 if firstParam == secondParam else 0
                base += 4
            elif opcode == 9:
                relativeBase += firstParam 
                base += 2
            elif opcode == 99:
                break
            else:
                print('Something went wrong, exiting')
                exit(1)
