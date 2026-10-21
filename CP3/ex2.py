def mostrar_tabuada(n1):
    for i in range(1,11):
        print(f"{n1} x {i} = {n1*i}")

while True:
    x = int(input("Digite um número (1 até 10): "))
    if x > 0 and x < 11:
        mostrar_tabuada(x)
        break
    else:
        print("Número invalido, digite apenas de 1 até 10")