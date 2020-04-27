#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    asteroidLocations = []
    with open('../inputs/test1.txt', 'r') as inputFile:
        for y, line in enumerate(inputFile):
            for x, i in enumerate(line):
                if i == '#':
                    asteroidLocations.append((x, y))
            maxX = x
        maxY = y
    
    #asteroidLocations = [(1,0), (4,0), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3), (3,4), (4,4)]
    #maxX = 4
    #maxY = 4
    asteroidsDetected = {}
    for x, y in asteroidLocations:
        numAsteroids = 0
        for x2, y2 in asteroidLocations:
            if x == x2 and y == y2:
                pass
            else:
                if x == x2: # Up/Down
                    start = y + (-1 if y > y2 else 1)
                    end = y2 + (-1 if y > y2 else 1)
                    step = -1 if y > y2 else 1
                    for t in range(start, end, step):
                        if (x, t) in asteroidLocations:
                            if t == y2:
                                numAsteroids += 1
                            else: # Blocked view
                                break
                elif y == y2: # Left/Right
                    start = x + (-1 if x > x2 else 1)
                    end = x2 + (-1 if x > x2 else 1)
                    step = -1 if x > x2 else 1
                    for t in range(start, end, step):
                        if (t, y) in asteroidLocations:
                            if t == x2:
                                numAsteroids += 1
                            else: # Blocked view
                                break
                else: # Diagonal
                    xDiff = max(x, x2) - min(x, x2)
                    yDiff = max(y, y2) - min(y, y2)
                    tX = float(x)
                    tY = float(y)
                    xStep = -(xDiff / yDiff) if x > x2 else xDiff / yDiff
                    yStep = -1 if y > y2 else 1
                    while tX != x2:
                        tX += xStep
                        tY += yStep
                        while not tX.is_integer():
                            tX += xStep
                            tY += yStep
                            if tX < 0 or tY < 0 or tX > maxX or tY > maxY:
                                break
                            
                        if (tX, tY) in asteroidLocations:
                            if tX == x2 and tY == y2:
                                numAsteroids += 1
                            else:
                                break
                        elif tX < 0 or tY < 0 or tX > maxX or tY > maxY:
                            break

        asteroidsDetected[(x, y)]= numAsteroids
    print('Highest number of asteroids detected from any location: {}'.format(max(asteroidsDetected.values())))
