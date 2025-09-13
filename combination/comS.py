def combinacao_simples(n, p):
    nFat = 1
    sub = n - p
    while n >= 1:
        nFat *= n
        n -= 1
    pFat = 1
    while p >= 1:
        pFat *= p
        p -= 1
    
    subFat = 1
    while sub >= 1:
        subFat *= sub
        sub -= 1
    divResult = nFat / (pFat * subFat)
    return divResult

print(combinacao_simples(4, 2))

