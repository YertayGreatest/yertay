def has_33(intlist):
    for i in range(0,len(intlist)-1):
        if intlist[i] == 3 and intlist[i] == intlist[i+1]:
            return True
    return False

        