def test(word, ch):
    s = ''
    temp = word.index(ch)
    i = temp
    while(temp >= 0):
        s += word[temp]
        temp -= 1
    s += word[i+1:]
    return s

test("abcdefd", "d")