def permutacao_simples(n):
    ps = 1
    while n >= 1:
        ps *= n
        n -= 1
    return ps
