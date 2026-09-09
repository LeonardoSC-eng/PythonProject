valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o Segundo valor: "))

print(f"\nANTES DA TROCA\nValor 1: {valor1}\nValor 2: {valor2}")

auxiliar = valor1
valor1 = valor2
valor2 = auxiliar

print(f"\nDEPOIS DA TROCA\nValor 1: {valor1}\nValor 2: {valor2}")