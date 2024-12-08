def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            
    while (left <= mid):
        temp.append(arr[left])
        left += 1
        
    while (right <= high):
        temp.append(arr[right])
        right += 1
        
    for i in range(low, high + 1):
        arr[i] = temp[i-low]
        
def mergersort(arr, low, high):
    if low >= high:
        return 
    mid = (low+high)//2
    mergersort(arr, low, mid)
    mergersort(arr, mid+1, high)
    merge(arr, low, mid, high)

arr = [9,5,6,7,4,1,8,2,3]
mergersort(arr, 0, len(arr)-1)
print(arr)
        
        
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]
    return quicksort(left) + middle + quicksort(right)

arr1 = [9,5,6,7,4,1,8,2,3]
arr1 = quicksort(arr1)
print(arr1)
        