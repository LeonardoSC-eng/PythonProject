#Criando uma lista
veiculos = ['Gol', 'Kwid', 'HB20', 'UP', 'Mobi']


#Acessar os elementos da lista


#Acesso Rápido: lista[indice]
print(veiculos[0])

#Recuperar e Alterar valores
veiculo = veiculos[3]
print(veiculo)

#Alterando um elemento da lista
veiculos[1] = 'BYD'
print(veiculos[1])

#Exibindo todos os itens da lista
print(veiculos)

#Trocando valores
veiculo1 = veiculos[1]
veiculo2 = veiculos[2]

veiculos[1] = veiculo2
veiculos[2] = veiculo1

print(veiculos)
