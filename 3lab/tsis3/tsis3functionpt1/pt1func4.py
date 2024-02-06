def filter_prime(aist):
    bist = []
    for num in aist:
        flag  = False
        if num>1:
            for i in range(2,num//2+1):
                if num%i==0:
                    flag = True
                    break
        if not flag:
            bist.append(num)
    return bist
filter_prime([23,44,56,88,93,17,101])