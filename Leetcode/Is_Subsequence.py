def isSubsequence(s, t):
    for i in s:
        if i in t:
            t = t[t.index(i)+1:]
        else:
            return False
    return True

s = "aec"
t = "abcde"

print(isSubsequence(s,t))