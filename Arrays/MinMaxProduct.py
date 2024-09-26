def fun(input1, input2):
    minimum_element = min(input1)
    for i in range(input2):
        input1[i] = (input1[i] - minimum_element) * minimum_element
    ans = '{'
    for i in range(len(input1)):
        if(i == len(input1)-1):
            ans += str(i)+'}'
        else:
            ans += str(i)+','
    return ans

s = input()
input2 = int(s[-1])
input1 = []
for i in s[:len(s)-2]:
    if i.isnumeric():
        input1.append(int(i))
print(fun(input1, input2))

    

