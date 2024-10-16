def intersect(nums1, nums2):
    ans = []
    for i in nums2:
        if i in nums1:
            nums1.remove(i)
            ans.append(i)
    return ans

print(intersect([1,2,2,1], [2,2]))
