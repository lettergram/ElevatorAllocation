# Python implemenation of Elevator Allocation Algorithm
# Written by Austin G. Walters for austingwalters.com
# July 2014 - Python 2.7

peoplePerFloor = 100.0
timePerFloor = 5
timePerWait = 20

# 3600 seconds per hours
rushHour = 3600.0

floorCount = 10
elevatorCount = 3

# Sets up the building, filling all the floors with people
def fillBuilding():
    building = []
    for i in range(floorCount - 1):
        building.append(peoplePerFloor)
    return building

# Determines the time for circuit (curr),
# as well as average carrying capacity per circuit.
# Given e - array of elevators, which holds the highest
# serviced floor, and i the current index of e.
def eleLoop(e, i):
    floorsServiced = e[i] - e[i-1] + 1
    cirTime = timePerFloor * e[i] * 2
    cirTime += timePerWait * floorsServiced
    avgCarry = cirTime * peoplePerFloor / rushHour * floorsServiced
    return cirTime, avgCarry

# (Index * 5 seconds) + (20 seconds * (Index - PrevIndex))
# If previous elevators loops/stops add up to be greater than,
# (timePerFloor * 2) + timePerWait, then increase floor of previous
# elevators loop. i.e. elevator[2]+=1   
def addFloor(e):
    choiceIndex = 0
    best = 9999
    for i in range(1, len(e)):
        cirTime, avgCarry = eleLoop(e, i)
        if cirTime + ((cirTime / 100) * avgCarry) < best:
            elevatorNumber = i
            best = cirTime + ((cirTime / 100) * avgCarry)
    for i in range(elevatorNumber, len(e)):
        e[i] += 1
    return e

# Prints the population of the buildings floor as an array.
def printApprox(building):
  str = '[  '
  for i in range(len(building)):
      str += '%06.3f  ' % building[i]
  str += ']'
  print str


# Prints the circuit(s) for each of the elevators
def printeleLoop(e):
    print ''
    print e
    print ''
    for i in range(1, len(e)):
        floorsServiced = e[i] - e[i-1] + 1
        curr = timePerFloor * e[i] * 2
        curr += timePerWait * floorsServiced
        avgCarry = curr * peoplePerFloor / rushHour * floorsServiced
        str = 'Elevator #%d, time for loop %d seconds, ' % (i, curr)
        str += 'carrying an average of '
        str += '%3.2f people per carry' % avgCarry
        print str
    print ''
    
# Allocate elevators
# Elevator[] represents the starting
# group of stops.
#
# i.e.
# If elevator[0]= 3 and elevator[1] = 5,
# elevator[0] visits floors 3 and 4.
# If elevator[1] = 7 instead,
# elevator[0] visits 3, 4, 5, and 6
def elevatorAllocation(building, elevatorCount):

    elevator = []
    for i in range(elevatorCount + 1):
        elevator.append(0)
    for i in range(1, floorCount):
        elevator = addFloor(elevator)
    printeleLoop(elevator)
    return elevator

def simulate(e, building):

    str = '[  '
    for floor in range(len(building)):
      str += 'floor%2d ' % (floor + 1)
    str += ']'
    print str

    eCircuit = []
    for i in range(len(e)):
        curr, avgCarry = eleLoop(e, i)
        eCircuit.append(float(curr))

    emptyFloors = 0
    iteration = 0
    finalFloor = 0

    while emptyFloors < len(building):
        emptyFloors = 0
        iteration += 1
        for i in range(1, len(e)):
            for j in range(e[i-1], e[i]):
                if building[j] > 0.0:
                    persons = eCircuit[i] * peoplePerFloor / rushHour
                    building[j] = building[j] - persons
                if 0 >= building[j]:
                    building[j] = 0.0
                    emptyFloors += 1
                    finalFloor = j
        printApprox(building)
    print ''

    # Find the final elevator on circuit, prints time
    for i in range(len(e)):
        if e[i] > finalFloor:
            iteration = eCircuit[i] * iteration / 60
    print 'Total Time: %d minutes\n' % (iteration)



# ___ MAIN ____

building = fillBuilding()
elevator = elevatorAllocation(building, elevatorCount)
simulate(elevator, building)
