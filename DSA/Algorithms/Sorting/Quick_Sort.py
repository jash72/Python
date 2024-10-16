import random

#method 1
def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = []
    right = []
    middle = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
    
    return QuickSort(left) + middle + QuickSort(right)

arr = [9,5,6,7,4,1,8,2,3]
arr = QuickSort(arr)
print(arr)

#method 2
def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr) # arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i >  pivot]
    middle = [i for i in arr if i == pivot]
    return Quicksort(left) + middle + Quicksort(right)
    