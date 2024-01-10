class Position:
    def __init__(self, name, numOfguards, guardingTime):
        """
        Initialize a Position object.

        Parameters:
        - name: Name of the position.
        - numOfguards: Number of guards associated with the position.
        - timeToGuard: Time duration for a guard shift in minutes.
        """
        self.name = name
        self.numOfGuards = numOfguards
        self.guardingTime = guardingTime
        self.stopper = guardingTime  # Countdown timer for guard shift
        self.guardList = []  # List to store guards assigned to the position

    def addGuard(self, name):
        """
        Add a guard to the position's guard list.

        Parameters:
        - name: Name of the guard to be added.
        """
        self.guardList.append(name)

    def pass5Minutes(self):
        """
        Simulate the passage of 5 minutes. Decrement the countdown timer.

        If the countdown timer reaches 0, reset it to the original timeToGuard.
        """
        self.stopper -= 5
        if self.stopper == 0:
            self.stopper = self.guardingTime

    def timeToSwitch(self):
        """
        Check if it's time to switch guards.

        Returns:
        - True if the countdown timer equals timeToGuard, indicating it's time to switch guards.
        - False otherwise.
        """
        return self.stopper == self.guardingTime

    def clearGuards(self):
        """
        Clear the list of guards for the position and reset the countdown timer to timeToGuard.
        """
        self.guardList = []
        self.stopper = self.guardingTime