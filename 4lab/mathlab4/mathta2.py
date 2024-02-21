import math
h = int(input("height: "))
a = int(input("first value: "))
b = int(input("second value: "))
def trapezoid(a,b,h):
    return (a+b)*h/2
print(trapezoid(a,b,h))