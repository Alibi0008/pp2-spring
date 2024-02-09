class Shape:
    def __init__(self):
        self.area = 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def getParameters(self):
        self.length = int(input())
        self.width = int(input())

    def calculateArea(self):
        self.area = self.length * self.width
        return self.area
    
a = Rectangle(0, 0)
a.getParameters()
print(a.calculateArea())