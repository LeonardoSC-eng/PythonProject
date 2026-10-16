#exemplo de função com retorno
#uma função não permite +1 de um retorno
def calcular_media(n1, n2):
    return (n1 + n2) / 2

#guardando o retorno dentro de uma variavel
media = calcular_media(10, 5)
print(media)

#chamado a função dentro do print
print(calcular_media(6, 20))