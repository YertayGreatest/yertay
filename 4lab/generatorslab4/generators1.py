def squaregenerator(N):
    for i in range(1, N+1):
        yield i**2
squares = squaregenerator(5)
for s in squares:
    print(s)