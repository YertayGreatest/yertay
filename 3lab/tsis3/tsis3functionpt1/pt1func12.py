def histogram(nums):
    result = ""
    for num in nums:
        result += "*" * num + " "
    return result
print(histogram([4,7,9]))
        