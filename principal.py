from arrangement.arrR import arranjo_com_repeticao
from arrangement.arrS import arranjo_simples
from combination.comR import combinacao_com_repeticao
from combination.comS import combinacao_simples
from permutation.perS import permutacao_simples

def menu():
    print(f"{'-=' * 10} MENU {'-=' * 10}")
    print("[1] Arranjo com repetição")
    print("[2] Arranjo sem repetição")
    print("[3] Combinação com repetição")
    print("[4] Combinação sem repetição")
    print("[5] Permutação sem repetição")
    print("[0] Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

while True:
    esc = menu()
    if esc == "0":
        print("Fim do programa!")
        break
    elif esc == "1":
        n = int(input("Valor de n: "))
        p = int(input("Valor de p: "))
        resultado = arranjo_com_repeticao(n, p)
        print(f"(ARRANJO COM REPETIÇÃO) Resultado: {resultado}")

    elif esc == "2":
        n = int(input("Valor de n: "))
        p = int(input("Valor de p: "))
        resultado = arranjo_simples(n, p)
        print(f"(ARRANJO SIMPLES) Resultado: {resultado}")

    elif esc == "3":
        n = int(input("Valor de n: "))
        p = int(input("Valor de p: "))
        resultado = combinacao_com_repeticao(n, p)
        print(f"(COMBINAÇÃO COM REPETIÇÃO) Resultado: {resultado}")
    elif esc == "4":
        n = int(input("Valor de n: "))
        p = int(input("Valor de p: "))
        resultado = combinacao_simples(n, p)
        print(f"(COMBINAÇÃO SIMPLES) Resultado: {resultado}")
    elif esc == "5":
        n = int(input("Valor de n: "))
        resultado = permutacao_simples(n)
        print(f"(PERMUTAÇÃO SIMPLES) Resultado: {resultado}")
    else:
        print(f"Opção '{esc}' inválida!")
    print()
