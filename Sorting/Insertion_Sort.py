def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = current

arr = [3, 6, 3, 2, -1, 34, 73, 12, 89, 334, 676]
insertionSort(arr)
print(arr)