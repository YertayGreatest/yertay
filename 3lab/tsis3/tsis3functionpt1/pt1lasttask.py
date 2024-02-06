'''
#gram to ounces
def gramtoounce(gram):
    return gram * 28.3495231

#farenheit to celcius
def fartocelc(farenheit):
    celc = (5/9) * (farenheit-32)
    return celc

#number of head and legs puzzle
def solve(heads, legs):
    rabbit = (legs - 2 * heads) / 2
    chicken = heads - rabbit
    print(chicken, rabbit)
'''
from pt1func1 import gramtoounce
from pt1func2 import fartocelc
from pt1func3 import solve
print(f"{100} grams is equal to {gramtoounce(100)} ounces")
print(f"{234} F is equal to {fartocelc(234)} C")
#etc