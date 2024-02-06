def spy_game(nums):
    for i in range(0,len(nums)-2):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False
print(spy_game([1,0,0,7,9]))