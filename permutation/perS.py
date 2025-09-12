def permutacao_simples(n):
    ps = 1
    while n >= 1:
        ps *= n
        print(f"VALOR DE 'PS': {ps}")
        n -= 1
    return ps

print(permutacao_simples(10))