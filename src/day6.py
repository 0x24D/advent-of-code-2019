#!/usr/bin/env python3

if __name__ == "__main__":
    # Part 1
    orbits = dict()
    with open('../inputs/day6.txt', 'r') as inputFile:
        for c, line in enumerate(inputFile):
            orbitee = line[:3]
            orbitor = line[4:7]
            orbits[orbitor] = orbitee

    totalOrbits = 0
    for o in orbits:
        directOrbit = orbits[o]
        while True:
            totalOrbits += 1
            try:
                directOrbit = orbits[directOrbit]
            except KeyError:
                break
    print("Number of direct and indirect orbits: {}".format(totalOrbits))

    # Part 2
    neighbours = {}
    for o in orbits:
        if o in neighbours:
            neighbours[o].append(orbits[o])
        else:
            neighbours[o] = [orbits[o]]
        if orbits[o] in neighbours:
            neighbours[orbits[o]].append(o)
        else:
            neighbours[orbits[o]] = [o]
    startingPlanet = neighbours['YOU'][0]
    finishingPlanet = neighbours['SAN'][0]

    # A* search algorithm from Wikipedia pseudocode
    openSet = {startingPlanet}
    cameFrom = {}
    gScore = {startingPlanet: 0}
    fScore = {startingPlanet: 1}

    while len(openSet) != 0:
        current = next(iter(openSet))
        if current == finishingPlanet:
            numberOfTransfers = 0
            while current in cameFrom:
                numberOfTransfers += 1
                current = cameFrom[current]
            print("Number of transfers from {} to {}: {}".format(
                startingPlanet, finishingPlanet, numberOfTransfers))
            break

        openSet.remove(current)
        for n in neighbours[current]:
            tenScore = gScore[current] + 1
            if n not in gScore or tenScore < gScore[n]:
                cameFrom[n] = current
                gScore[n] = tenScore
                fScore[n] = gScore[n] + 1
                if n not in openSet:
                    openSet.add(n)
