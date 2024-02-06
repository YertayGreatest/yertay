def unique(nums):
    uniqueelems = []
    for i in nums:
        if i not in uniqueelems:
            uniqueelems.append(i)
        else:
            continue
    return uniqueelems
