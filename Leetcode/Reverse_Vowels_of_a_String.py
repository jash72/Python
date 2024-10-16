def stringReverse(s):
    t = 'aeiou'
    left = 0
    right = len(s) - 1 

    while left <= right:
        if s[left].lower() not in t:
            left += 1
        while s[right].lower() in t and left <= right:
            right -= 1

        if left <= right:
            m = s[left]
            s = s[:left - 1] + s[right] + s[left+1:right-1] + m + s[right+1:]
            print(s)
            left += 1
            right -= 1
    print(s)


s = "IceCreAm"
stringReverse(s)
print(s)