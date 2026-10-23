pokemons = ['Pikachu', 'Mew', 'Abra', 'Charmander', 'Rayquaza', 'Dragonite']
print(pokemons, len(pokemons))

#append(valor): adicionar itens no fim da lista

pokemons.append("Mewtwo")
pokemons.append("Articuno")
pokemons.append("Zapdos")
pokemons.append("Moltres")
pokemons.append("Ho-ho")

print(pokemons, len(pokemons))

#insert(indice, valor): adicionar um item atraves de uma posição

pokemons.insert(1, "gengar")
print(pokemons, len(pokemons))

#extend([valor, valor, valor]): adicionar multiplos itens
pokemons.extend(['Eevee', 'Charizard', 'Caterpie'])

#pop(index): remover item da lista por base do index

pokemons.pop(3)
print(pokemons, len(pokemons))

#reverse
pokemons.reverse()
print(pokemons, len(pokemons))

#sort: ordenar valores de uma lista no modo crescente(A-Z, 0-n, etc)
pokemons.sort()
print(pokemons, len(pokemons))

#remove(valor): remove um item da lista com base do valor

pokemons.remove("Mewtwo")
print(pokemons, len(pokemons))

#del(index): remover item da lista por base do intervalo do index
del pokemons[1:3] #1 até o 3
print(pokemons, len(pokemons))

#clear(): limpar a lista
pokemons.clear()
print(pokemons, len(pokemons))