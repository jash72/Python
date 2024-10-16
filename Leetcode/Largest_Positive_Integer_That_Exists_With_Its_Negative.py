def findMaxK( nums):
    if len(nums) <= 0:
        return -1
    if max(nums) * (-1) in nums:
        return max(nums)
    else:
        nums.remove(max(nums))
        return findMaxK(nums)
 #solved using recursion
 # else try this for leetcode
"""

def findMaxK( nums):
    while(len(nums) > 1):
        if max(nums) * (-1) in nums:
            return max(nums)
        else:
            nums.remove(max(nums))
    return -1

"""
nums = [10,6,7,1]
print(findMaxK(nums))