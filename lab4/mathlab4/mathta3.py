import math
sides = int(input("sides: "))
lengthofside = int(input("length of side: "))
def arearegularpoly(sides, length):
    perimeter = sides * length
    apothem = length/(2 * math.tan(math.pi/sides))
    return perimeter * apothem / 2
print(arearegularpoly(sides, lengthofside))