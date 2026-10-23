def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

for i in range(1, 6):
    num = int(input("Digite um valor: "))

    if eh_par(num) == True:
        print("Par")
    else:
        print("Impar")