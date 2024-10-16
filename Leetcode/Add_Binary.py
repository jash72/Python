def fun(a, b):
    num1 = 0
    num2 = 0
    ii = 0
    jj = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1':
            num1 += 2 ** ii
        ii += 1

    for j in range(len(b)-1, -1, -1):
        if b[j] == '1':
            num2 += 2 ** jj
        jj += 1

    return str(bin(num1 + num2))[2:]
a = "1010"
b = "1011"
print(fun(a, b))