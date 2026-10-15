qntImpar = 0
qntPar = 0
totalPar = 0
totalImpar = 0

while True:
    valor = int(input("Digite um valor ou digite 0 para somar: "))
    if valor == 0:
        totalPar = totalPar / qntPar
        totalImpar = totalImpar / qntImpar
        print(f"A média do calculo dos números pares é de: {totalPar} \n"
              f"A média do calculo dos números impares é de: {totalImpar}")
        break
    else:
        if valor % 2 == 0:
            qntPar += 1
            totalPar = valor + totalPar
        else:
            qntImpar += 1
            totalImpar = valor + totalImpar
