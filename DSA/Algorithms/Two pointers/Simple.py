def fun(l, target):
    i = 0
    j = len(l) - 1
    while(i < j):
        if(l[i] + l[j] == target):
            h = 0
            print(l[i], l[j])
            return i, j
        elif(l[i] + l[j] < target):
            i += 1
        elif(l[i] + l[j] > target):
            j -= 1
    return -1

l = [-4, -2, 0, 2, 4, 5, 5, 7, 9, 11, 14]
target = 10
print(fun(l, target))
#When an array is sorted order then use two pointers algorithm.