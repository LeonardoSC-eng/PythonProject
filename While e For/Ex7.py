contador = 0
while contador <10:
    contador += 1

    if contador == 5:
        print("pulei o 5!")
        continue #Forçar o laço realizar a verificação da condição (ou pular um loop)

    print(contador)

print("Fora do laço")