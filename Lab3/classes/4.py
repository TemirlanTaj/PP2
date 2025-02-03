class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'x coordinate: {self.x}, y coordinate: {self.y}')
    def dist(p1, p2):
        return ( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 ) ** 0.5
    
tochka1 = Point(1,2)
tochka2 = Point(4,5)

tochka1.show()
tochka2.show()
print(tochka1.dist(tochka2))