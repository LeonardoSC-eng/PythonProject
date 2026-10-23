#Lista dentro de lista (ou Matriz)

#Uma matriz 3x3 (3 linhas e 3 colunas)
matriz = [
    [1,2,3], #linha 0
    [4,5,6], #linha 1
    [7,8,9]  #linha 2
]

# Acessar uma matriz
print(matriz[0][2])
print(matriz[1][2])

print("Percorrendo uma matriz")
for linha in matriz:
    for coluna in linha:
        print(coluna, end=" ")
    print() #Pular linha