import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("coordinates: ", self.x, self.y)
    def move(self, nx, ny):
        self.x = nx
        self.y= ny
    def dist(self, difpoint):
        a = self.x - difpoint.x
        b = self.y - difpoint.y
        return round(math.sqrt(a**2 + b**2), 5)

point1 = Point(1,2)
point2 = Point(5,6)
point1.show()
point2.move(8,10)
point2.show()
print(point1.dist(point2))
    
