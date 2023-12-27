class Position:
    def __init__(self, name, numOfguards, timeToGuard):
        self.name = name
        self.numOfGuards = numOfguards
        self.timeToGuard = timeToGuard
        self.stopper = timeToGuard
        self.guardList = []

    def addGuard(self, name):
        self.guardList.append(name)

    def pass5Minutes(self):
        self.stopper -= 5
        if self.stopper == 0:
            self.stopper = self.timeToGuard

    def timeToSwitch(self):
        return self.stopper == self.timeToGuard

    def clearGuards(self):
        self.guardList = []
        self.stopper = self.timeToGuard




