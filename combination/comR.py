def combinacao_com_repeticao(n, p):
    numerador = n + p - 1
    numeradorFat = 1
    while numerador >= 1:
        numeradorFat *= numerador
        numerador -= 1
    
    pFat = 1
    while p >= 1:
        pFat *= p
        p -= 1
    
    denominador = n - 1
    denominadorFat = 1
    while denominador >= 1:
        denominadorFat *= denominador
        denominador -= 1
    
    divResult = numeradorFat / (pFat * denominadorFat)
    return divResult

print(combinacao_com_repeticao(2, 3))
    
