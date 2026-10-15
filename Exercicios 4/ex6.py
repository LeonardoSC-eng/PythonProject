menorValor = int(input("Digite o 1° número: "))

for i in range(2, 10):
    num = int(input(f"Digite o {i+1}° número: "))
    if num < menorValor:
        menorValor = num
print(f"O menor valor é {menorValor}")