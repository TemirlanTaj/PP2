class Shape:
    def area(self):
        return 0
        

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
figura1 = Shape()

print(figura1.area())

figura2 = Square(4)

print(figura2.area())