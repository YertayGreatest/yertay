def downton(n):
    for i in range(n,-1,-1):
        yield i
n=6
for i in downton(n):
    print(i)