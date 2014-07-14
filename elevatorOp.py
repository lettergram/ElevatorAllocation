# Python implemenation of Elevator Allocation Algorithm
# Written by Austin G. Walters for austingwalters.com
# July 2014 - Python 2.7

peoplePerFloor = 100
timePerFloor = 5
timePerWait = 20

floorCount = 12
elevatorCount = 3

# Sets up the building, filling all the floors with people
def fillBuilding(floorCount):
    building = []
    for i in range(floorCount):
        building.append(peoplePerFloor)
    return building

def addFloor(e):

    choiceIndex = 0
    best = 999

    for i in range(1, len(e)):
        
        floorsServiced = e[i] - e[i-1]
        
        curr = timePerFloor * e[i] * 2
        curr += timePerWait * floorsServiced
    
        if curr < best:
            choiceIndex = i
            best = curr    

    for i in range(choiceIndex, len(e)):
        e[i] += 1

    return e


def elevatorAllocation(building, elevatorCount):

    # Allocate elevators
    # Elevator[] represents the starting
    # group of stops. 
    #
    # i.e. 
    # If elevator[0]= 3 and elevator[1] = 5,
    # elevator[0] visits floors 3 and 4.
    # If elevator[1] = 7 instead,
    # elevator[0] visits 3, 4, 5, and 6
    elevator = []
    for i in range(elevatorCount + 1):
        elevator.append(0)

    # (Index * 5 seconds) + (20 seconds * (Index - PrevIndex))
    # If previous elevators loops/stops add up to be greater than,
    # (timePerFloor * 2) + timePerWait, then increase floor of previous
    # elevators loop. i.e. elevator[2]++
    for i in range(1, floorCount):
        print ('floor', i)
        elevator = addFloor(elevator)
    
    print elevator
    
    return building 

#def simulate(elevator, building):
    # nothing atm

building = fillBuilding(floorCount)

print elevatorAllocation(building, 3)
