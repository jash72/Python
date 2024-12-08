def maximumSwap(num):
        l = list(str(num))
        for i in range(len(l)):
            l[i] = int(l[i])
        max_num = l.index(max(l))
        temp = l[max_num]
        l[max_num] = l[0]
        l[0] = temp
        s = ''
        for i in range(len(l)):
            s += str(l[i])
        return int(s)
num = 2736
print(maximumSwap(num))