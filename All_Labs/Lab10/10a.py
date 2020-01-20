import math

class Circle:



    def __init__(self,r=1):
        self.radius = r

    def setRadius(self,r):
        self.__radius = r

    def getCircumference(self):
        return 2*math.pi*self.__radius

    def getArea(self):
        return math.pi*self.__radius*self.__radius

newcircle = Circle()
newcircle.setRadius(3)
print(newcircle.getCircumference())
print(newcircle.getArea())
