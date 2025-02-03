from classShape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

figura3 = Rectangle(4, 5)

print(figura3.area())
