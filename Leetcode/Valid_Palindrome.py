def isPalindrome(s):
    t = ''
    for i in s.lower():
        if i >= 'a' and i <= 'z':
            t += i
    return t[::-1] == t

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
