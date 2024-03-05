s = input("string: ")
upps = 0
lows = 0
for i in s:
    if i == i.upper():
        upps += 1
    else:
        lows += 1
print(upps, lows)