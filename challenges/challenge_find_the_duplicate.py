def find_duplicate(nums):
    if len(nums) < 2 or type(nums) != list:
        return False
    nums.sort()
    for i in range(0, len(nums) - 1):
        if type(nums[i]) != int or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False


# print(find_duplicate([1, 3, 4, 5, 2]))
