def fun(firstWord, secondWord, targetWord):
    s = 'abcdefghijklmnopqrstuvwxyz'
    f1 = ''
    f2 = ''
    f3 = ''
    for i in firstWord:
        f1 += str(s.index(i))
    for i in secondWord:
        f2 += str(s.index(i))
    for i in targetWord:
        f3 += str(s.index(i))
    if int(f3) == int(f1) + int(f2):
        return True
    return False
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(fun(firstWord, secondWord, targetWord))