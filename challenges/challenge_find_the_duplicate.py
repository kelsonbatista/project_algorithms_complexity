def find_duplicate(nums):
    if len(nums) < 2: return False
    if type(nums) != list: return False
    for i in range(0, len(nums) - 1):
        if type(nums[i]) != int: return False
        if nums[i] < 0: return False
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]: return nums[i]
    return False
    

# print(find_duplicate([1, 3, 4, 2, 2]))
