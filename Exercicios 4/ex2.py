qntMenor = 0
qntTotal = 0

while True:
    if qntTotal < 10:
        idade = int(input(f"Digite a {qntTotal+1}° idade: "))
        if idade < 18:
            qntMenor += 1
        qntTotal += 1
    else:
        print(f"A quantidade de menores de idade é: {qntMenor}")
        break

