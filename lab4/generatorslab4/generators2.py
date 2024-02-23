def evens(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input("num: "))
evengens = evens(n)
evenlist = list(evengens)
print(", ".join(map(str, evenlist)))
