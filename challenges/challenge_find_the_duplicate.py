def validate(nums):
    if len(nums) < 2 or type(nums) != list:
        return False


def sort_nums(nums):
    n = len(nums)
    for i in range(n - 1):
        for item in range(0, n - 1 - i):
            if nums[item] > nums[item + 1]:
                current = nums[item]
                nums[item] = nums[item + 1]
                nums[item + 1] = current
    return nums


def find_duplicate(nums):
    validate(nums)
    ordered = sort_nums(nums)
    for i in range(0, len(ordered) - 1):
        if type(nums[i]) != int or nums[i] < 0:
            return False
        if ordered[i] == ordered[i + 1]:
            return ordered[i]
    return False


# def find_duplicate(nums):
#     validate(nums)
#     for i in range(0, len(nums) - 1):
#         if type(nums[i]) != int or nums[i] < 0:
#             return False
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return nums[i]
#     return False


# print(find_duplicate([1, 3, 4, 2, 2]))
