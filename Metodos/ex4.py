
def alterar(n1):
    x = n1
    print(x)
#x é uma variavel local
#x é uma desconhecido por todo o códico
#apenas essa função tem conhecimento de x

#chamando uma variavel local fora da função
# print(x) -> ira causar erro de localização de variavel (ela não existe)

alterar(10)