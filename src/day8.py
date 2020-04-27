#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    with open('../inputs/day8.txt', 'r') as inputFile:
        imageData = [[]]
        pixelsWide, pixelsTall = (25, 6)
        while True:
            row = inputFile.read(pixelsWide)
            if row and row != '\n':
                if len(imageData[-1]) == pixelsTall:
                    imageData.append([row])
                else:
                    imageData[-1].append(row)
            else:
                break

    layerData = [pixelsWide * pixelsTall + 1, 0]
    for layer in imageData:
        numZero = 0
        numOne = 0
        numTwo = 0
        for row in layer:
            for i in row:
                if int(i) == 0:
                    numZero += 1
                elif int(i) == 1:
                    numOne += 1
                elif int(i) == 2:
                    numTwo += 1
        if layerData[0] > numZero:
            layerData[0] = numZero
            layerData[1] = numOne * numTwo
    print('Number of 1 digits * number of 2 digits = {}'.format(layerData[1]))

    # Part 2
    # imageData = [l1: ['r1', 'r2', 'r3', 'r4', 'r5', 'r6'], l...: [...]]
    # completeImage = [r1: ['p1', 'p2', 'p3', 'p4', 'p5' ...], r...: [...]]
    completeImage = [[' '] * pixelsWide for i in range(pixelsTall)]
    for l in imageData:
        for y, _ in enumerate(completeImage):
            for x, _ in enumerate(completeImage[y]):
                if completeImage[y][x] == ' ':
                    d = int(l[y][x])
                    completeImage[y][x] = '_' if d == 0 else '#' if d == 1 else ' '

    print('Decoded image:')
    for i in completeImage:
        for j in i:
            print(j, end='')
        print('')
