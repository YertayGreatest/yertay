from time import sleep
import math
num = float(input(""))
delay = float(input(""))

sleep(delay/1000)
print(f'square root of {num} after {delay} miliseconds is {math.sqrt(num)}')
