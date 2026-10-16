x = 0

def alterar(n1):
   # x = n1 #Redeclarando -> não substitui o valor da variavel global
    global x #Substituindo o valor de x
    x = n1
    print(x)

alterar(10)
print(x)