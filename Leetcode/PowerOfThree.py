def powerOfThree(n):
    if n == 1:
        return 'true'
    elif n <= 0:
        return 'false'
    return powerOfThree(n/3)
print(powerOfThree(-1))