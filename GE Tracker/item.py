import datetime

class item():
    def __init__(self, name):
        self.name = name
        self.overallAverage = 0
        self.change = 0
        self.priceTracker = [] #price, dateStamp

    def setChange(self):
        for i in range(len(self.priceTracker)):
            if self.priceTracker[len(self.priceTracker)-(i+1)][0] != self.overallAverage:
                self.change = self.overallAverage - self.priceTracker[len(self.priceTracker)-(i+1)][0]
                break
