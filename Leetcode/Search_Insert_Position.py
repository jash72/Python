def fun(arr, K):
    start = 0
    end = len(arr) - 1
 
    while start<= end:
 
        mid =(start + end)//2
 
        if arr[mid] == K:
            return mid
 
        elif arr[mid] < K:
            start = mid + 1
        else:
            end = mid-1
 
    return end + 1
nums = [1, 3, 5]
target = 4
print(fun(nums, target))
    
