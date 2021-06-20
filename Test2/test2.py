for i in range(11, 80):
    if i % 3 == 0 and i % 5 == 0:
        i = "$$@@"
    elif i % 5 == 0:
        i = "@@"
    elif i % 3 == 0:
        i = "$$"
    print(i)
