for i in range(3**4):
    res = []
    for j in range(4):
        mm = i % 3
        i //= 3
        res.append(mm)
    print(res)
        