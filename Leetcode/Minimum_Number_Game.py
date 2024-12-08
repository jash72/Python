def fun(nums):
    l = []
    while(len(nums) > 0):
        n = min(nums)
        nums.remove(n)
        m = min(nums)
        nums.remove(m)
        l.append(m)
        l.append(n)
    return l
nums = [5,4,2,3]
print(fun(nums))