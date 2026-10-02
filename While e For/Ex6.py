contador = 1
while contador <=10:

    print(contador)

    if contador == 5:
        print("Achei o 5!")
        break #Forçando a parada do loop

    contador += 1

print("Fora do laço")