from random import shuffle
import time

from Position import Position


class Shavtzak:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.guardList = []
        self.positionList = []
        self.time = []

    def addGuard(self, name):
        self.guardList.append(name)

    def randomOrder(self):
        shuffle(self.guardList)

    def addPosition(self, position):
        self.positionList.append(position)

    def createGuardsList(self):
        self.createClock()
        indexGuard = 0
        for i in range(len(self.time)):
            for j in range(len(self.positionList)):
                if self.positionList[j].timeToSwitch():
                    str = self.time[i] + " "
                    for z in range(0, self.positionList[j].numOfGuards):
                        str += self.guardList[indexGuard] + " "
                        indexGuard += 1
                        if indexGuard == len(self.guardList):
                            indexGuard = 0

                    self.positionList[j].addGuard(str)
                self.positionList[j].pass5Minutes()

        self.printShavtzak()

    def createClock(self):
        count24 = 0
        while count24 < 24:

            # Check if the minute reaches 60 and reset it to 0
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                count24 += 1

                # Check if the hour reaches 24 and reset it to 0
                if self.hour == 24:
                    self.hour = 0

            # Append the current hour and minute as a string to the time list
            self.time.append(f"{self.hour:02d}:{self.minute:02d}")

            self.minute += 5

    def printGuardsList(self):
        print(self.guardList)

    def printPositionsList(self):
        for i in self.positionList:
            print(f'{i.name} ')

    def printShavtzak(self):
        for position in self.positionList:
            print(position.name)
            print(position.guardList)

def main():
    # Create instances of Shavtzak
    shavtzak_instance = Shavtzak(0, 0)

    # Add guards to Shavtzak
    shavtzak_instance.addGuard("Guard1")
    shavtzak_instance.addGuard("Guard2")
    shavtzak_instance.addGuard("Guard3")
    shavtzak_instance.addGuard("Guard4")
    shavtzak_instance.addGuard("Guard5")
    shavtzak_instance.addGuard("Guard6")
    shavtzak_instance.addGuard("Guard7")
    shavtzak_instance.addGuard("Guard8")
    shavtzak_instance.addGuard("Guard9")

    # Add positions to Shavtzak
    position1 = Position("Position1", 1, 60)
    position2 = Position("Position2", 2, 90)

    shavtzak_instance.addPosition(position1)
    shavtzak_instance.addPosition(position2)

    # Create random order for guards
    # shavtzak_instance.randomOrder()

    # Create clock and guards list
    # shavtzak_instance.createClock()
    shavtzak_instance.createGuardsList()

    # Print results
    # print("Time:", shavtzak_instance.time)
    # for position in shavtzak_instance.positionList:
    #     #     print(f"{position.name} Guards:", position.guardList)
    # shavtzak_instance.printShavtzak()
    # shavtzak_instance.printPositionsList()

if __name__ == "__main__":
    main()

