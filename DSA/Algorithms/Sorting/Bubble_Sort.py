def bubbleSort(arr):
    while True:
        flag = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        if(flag != True):
            break

#using for loop:
def bubbleSortFor(arr):
    for j in range(len(arr)-1):
        for i in range(0, len(arr)-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print("For loop",arr)
'''
time complexity: n*(n-1)//2
'''
arr = [3, 6, 3, 2, -1, 34, 73, 12, 89, 334, 676]
#bubbleSort(arr)
bubbleSortFor(arr)
print(arr)


            


def search(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)- i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

