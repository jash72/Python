def SelectionSort(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[min_pos] > arr[j]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

arr = [9,5,6,7,4,1,8,2,3]
SelectionSort(arr)
print(arr)
