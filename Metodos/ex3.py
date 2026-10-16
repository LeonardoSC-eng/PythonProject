#função com variavel global, sendo redeclarada
def alterar(n1):
    n1 = n1 + 1
    print(f"Dentro da função: {n1}")

x = 10

alterar(x)

print(f"Fora da função: {x}")