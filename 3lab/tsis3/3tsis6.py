'''def prime(aist):
    filtrated = []
    for num in aist:
        
        flag = False
        for i in range(2,num):
            if num%i==0 and num<=1:
                flag = True
                break
        if flag == False:
            filtrated.append(num)
    print(filtrated)

prime([1,2,3,4,5,6,7])
'''

prime = lambda x: x>1 and all(x%i!=0 for i in range(2, (x//2)))
numbers = [1,2,3,4,5,6,7,8,9,10,11]
print(list(filter(prime, numbers)))        
    