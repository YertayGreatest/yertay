def gendivby34(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            yield i
n = 24
nums = gendivby34(n)
for num in nums:
    print(num)