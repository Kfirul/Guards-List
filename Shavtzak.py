from random import shuffle
import time

from Position import Position  # Assuming Position class is defined in a separate module

class Shavtzak:
    def __init__(self, hour, minute):
        """
        Initialize a Shavtzak instance.

        Parameters:
        - hour: Starting hour for the Shavtzak.
        - minute: Starting minute for the Shavtzak.
        """
        self.hour = hour
        self.minute = minute
        self.guardList = []  # List to store guards
        self.positionList = []  # List to store positions
        self.time = []  # List to store time intervals

    def addGuard(self, name):
        """
        Add a guard to the Shavtzak's guard list.

        Parameters:
        - name: Name of the guard to be added.

        Returns:
        - True if the guard was successfully added.
        - False if the guard already exists.
        """
        if name not in self.guardList:
            self.guardList.append(name)
            return True
        else:
            return False

    def deleteGuard(self, name):
        """
        Delete a guard from the Shavtzak's guard list.

        Parameters:
        - name: Name of the guard to be deleted.

        Returns:
        - True if the guard was successfully deleted.
        - False if the guard does not exist.
        """
        if name in self.guardList:
            self.guardList.remove(name)
            return True
        else:
            return False

    def randomOrder(self):
        """
        Shuffle the order of guards randomly.
        """
        shuffle(self.guardList)

    def addPosition(self, position):
        """
        Add a position to the Shavtzak's position list.

        Parameters:
        - position: Instance of the Position class to be added.

        Returns:
        - True if the position was successfully added.
        - False if the position with the same name already exists.
        """
        if position.name not in [p.name for p in self.positionList]:
            self.positionList.append(position)
            return True
        else:
            return False

    def deletePosition(self, name):
        """
        Delete a position from the Shavtzak's position list.

        Parameters:
        - name: Name of the position to be deleted.

        Returns:
        - True if the position was successfully deleted.
        - False if the position does not exist.
        """
        for position in self.positionList:
            if position.name == name:
                self.positionList.remove(position)
                return True
        return False

    def createGuardsList(self):
        """
        Create a schedule for guards based on positions and time intervals.
        """
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
                        if z == self.positionList[j].numOfGuards -1:
                            str += self.guardList[indexGuard]
                        else:
                            str += self.guardList[indexGuard] + ", "
                        indexGuard += 1
                        if indexGuard == len(self.guardList):
                            indexGuard = 0

                    self.positionList[j].addGuard(str)
                self.positionList[j].pass5Minutes()

    def createClock(self):
        """
        Create a clock with time intervals at 5-minute intervals.
        """
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
        """
        Print the list of guards in the Shavtzak.
        """
        print(self.guardList)

    def printPositionsList(self):
        """
        Print the list of positions in the Shavtzak.
        """
        for i in self.positionList:
            print(f'{i.name} ')

    def printShavtzak(self):
        """
        Print the guards assigned to each position in the Shavtzak.
        """
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
    position3 = Position("Position3", 2, 90)


    shavtzak_instance.addPosition(position1)
    shavtzak_instance.addPosition(position2)

    shavtzak_instance.createGuardsList()
    # shavtzak_instance.printPositionsList()

    shavtzak_instance.printShavtzak()
    # shavtzak_instance.printGuardsList()
    print("--------")
    shavtzak_instance.deletePosition("Position2")
    shavtzak_instance.deleteGuard("Guard1")
    shavtzak_instance.createGuardsList()
    shavtzak_instance.printShavtzak()
    # shavtzak_instance.printPositionsList()



if __name__ == "__main__":
    main()