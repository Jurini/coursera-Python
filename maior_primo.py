def ePrimo(k):
    i = 0
    while i < k:
        i = i + 1
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            mp = i
    return mp


print(ePrimo(100))
