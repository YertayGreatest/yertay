import math
degree = int(input("degree: "))
def degreetoradian(degree):
    return degree * math.pi / 180
print(degreetoradian(degree))