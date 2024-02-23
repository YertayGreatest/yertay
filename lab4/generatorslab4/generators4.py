def squaresgen(a, b):
    for i in range(a,b+1):
        yield i**2
        
a=2
b=7
for s in squaresgen(a,b):
    print(s)