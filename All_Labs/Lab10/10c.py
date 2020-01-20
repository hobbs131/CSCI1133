from time import time
import random

class Stopwatch:
    def __init__(self, startTime = time(), endTime = time()):
        self.startTime= startTime
        self.endTime = endTime

    def start(self):
        self.startTime = time()

    def stop(self):
        self.endTime = time()

    def elapsedTime(self):
        return float(self.endTime-self.startTime)

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime
def main():

    list = ['9']*10000
    stopwatch = Stopwatch()
    print(stopwatch.getStartTime())
    stopwatch.start()
    list.sort()
    stopwatch.stop()
    print(stopwatch.getEndTime())
