veiculos = ['Gol', 'Kwid', 'HB20', 'UP', 'Mobi']

#Acesso posicional
#For-each
#for item in nome_lista:

print("Percorrendo uma lista com for-each: ")

i=0
for item in veiculos:
    print(f"{i} : {item}")
    i=i+1

#Obter o tamanho da lsita
print("Tamanho da lista é: ", len(veiculos))
#Ou for
#for i in range(len(lista))

print("Percorrendo uma lista com for: ")
for i in range(len(veiculos)):
    print(f"{i} : {veiculos[i]}")


#Ou while
#while i < len(lista):

print("Percorrendo uma lista com while: ")
ii = 0
while ii < len(veiculos):
    print(f"{ii} : {veiculos[ii]}")
    ii+=1
