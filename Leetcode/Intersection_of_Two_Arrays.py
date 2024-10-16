def intersection(nums1, nums2):
    ans = []
    for i in list(set(nums2)):
        if i in list(set(nums1)):
            ans.append(i)
    return ans

print(intersection([1,2,2,1], [2,2]))


#simple one
"""

return list(set(nums1).intersection(set(nums2))

"""