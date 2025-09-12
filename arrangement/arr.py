def arranjo(n, p):
    nFat = 1
    sub = n - p
    while n >= 1:
        nFat *= n
        n -= 1

    subFat = 1

    while sub >= 1:
        subFat *= sub
        sub -= 1
    devResult = nFat / subFat      
    return devResult

print(arranjo(12, 3))