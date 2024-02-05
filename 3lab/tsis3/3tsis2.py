class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square:
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

instance = Square(5)
sqarea = instance.area()
print("Area of square: ", sqarea)
shapeins = Shape()
shapearea = shapeins.area()
print("Area of shape", shapearea)

            