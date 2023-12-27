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
        if name not in self.guardList:
            self.guardList.append(name)
            return True  # Indicates that the guard was successfully added
        else:
            return False  # Indicates that the guard already exists

    def randomOrder(self):
        shuffle(self.guardList)

    def addPosition(self, position):
        if position.name not in [p.name for p in self.positionList]:
            self.positionList.append(position)
            return True
        else:
            return False

    def createGuardsList(self):
        self.randomOrder()
        self.createClock()
        indexGuard = 0

        for position in self.positionList:
            position.clearGuards()

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

        # self.printShavtzak()

    def createClock(self):
        increaseHour = self.hour
        increaseMinute = self.minute
        count24 = 0
        while count24 < 24:

            # Check if the minute reaches 60 and reset it to 0
            if increaseMinute == 60:
                increaseMinute = 0
                increaseHour += 1
                count24 += 1

                # Check if the hour reaches 24 and reset it to 0
                if increaseHour == 24:
                    increaseHour = 0

            # Append the current hour and minute as a string to the time list
            self.time.append(f"{increaseHour:02d}:{increaseMinute:02d}")

            increaseMinute += 5

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
    shavtzak_instance = Shavtzak(18, 00)

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

    shavtzak_instance.createGuardsList()
    shavtzak_instance.printShavtzak()

    shavtzak_instance.createGuardsList()
    shavtzak_instance.printShavtzak()

if __name__ == "__main__":
    main()

