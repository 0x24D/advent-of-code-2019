#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    import itertools
    with open('../inputs/day7.txt', 'r') as inputFile:
        intCodeStr = inputFile.read()
    highestSignal = -1
    for p in list(itertools.permutations([0, 1, 2, 3, 4])):
        inputBuffer = {
            '0': [0, p[0]],
            '1': [],
            '2': [],
            '3': [],
            '4': []
        }

        for a in range(5):
            intCodeArr = list(map(int, intCodeStr.split(',')))
            skipTo = 0
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
                            intCodeArr[intCodeArr[i + 1]
                                       ] = inputBuffer[str(a)].pop()
                        else:
                            intCodeArr[i + 1] = inputBuffer[str(a)].pop()
                        skipTo = i + 2
                    elif opcode == 4:
                        outputBuffer = intCodeArr[intCodeArr[i + 1]
                                                  ] if firstParamMode == 0 else intCodeArr[i + 1]
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
                    elif opcode == 99:
                        if a == 4:
                            if highestSignal < outputBuffer:
                                highestSignal = outputBuffer
                        else:
                            inputBuffer[str(a + 1)] = [outputBuffer, p[a + 1]]
                        break
                    else:
                        print('Something went wrong, exiting')
                        exit(1)
    print('Highest signal from initial loop: {}'.format(highestSignal))

    # Part 2
    def runAmp(a, inputQueue, outputQueue):
        import itertools
        import time
        with open('../inputs/day7.txt', 'r') as inputFile:
            intCodeStr = inputFile.read()
        intCodeArr = list(map(int, intCodeStr.split(',')))
        skipTo = 0
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
                    while inputQueue.empty():
                        pass
                    val = inputQueue.get()
                    if firstParamMode == 0:
                        intCodeArr[intCodeArr[i + 1]
                                   ] = val
                    else:
                        intCodeArr[i + 1] = val
                    skipTo = i + 2
                elif opcode == 4:
                    val = intCodeArr[intCodeArr[i + 1]
                                     ] if firstParamMode == 0 else intCodeArr[i + 1]
                    outputQueue.put(val)
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
                elif opcode == 99:
                    break
                else:
                    print('Something went wrong, exiting')
                    exit(1)

    from threading import Thread
    from queue import Queue

    for p in list(itertools.permutations([5, 6, 7, 8, 9])):
        oneTwoQueue = Queue()
        twoThreeQueue = Queue()
        threeFourQueue = Queue()
        fourFiveQueue = Queue()
        fiveOneQueue = Queue()
        fiveOneQueue.put_nowait(p[0])
        fiveOneQueue.put_nowait(0)
        oneTwoQueue.put_nowait(p[1])
        twoThreeQueue.put_nowait(p[2])
        threeFourQueue.put_nowait(p[3])
        fourFiveQueue.put_nowait(p[4])
        amp1 = Thread(target=runAmp, args=(0, fiveOneQueue, oneTwoQueue,))
        amp2 = Thread(target=runAmp, args=(1, oneTwoQueue, twoThreeQueue,))
        amp3 = Thread(target=runAmp, args=(2, twoThreeQueue, threeFourQueue,))
        amp4 = Thread(target=runAmp, args=(3, threeFourQueue, fourFiveQueue,))
        amp5 = Thread(target=runAmp, args=(4, fourFiveQueue, fiveOneQueue,))

        amp1.start()
        amp2.start()
        amp3.start()
        amp4.start()
        amp5.start()
        amp5.join()

        outputVal = fiveOneQueue.get()
        if highestSignal < outputVal:
            highestSignal = outputVal

    print('Highest signal from feedback loop: {}'.format(highestSignal))
