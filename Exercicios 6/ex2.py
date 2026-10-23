def exibir_media(nota1, nota2):
   print((nota1 + nota2) / 2)

def calcular_media(nota1, nota2):
    nota1 = (nota1 + nota2) / 2
    return nota1

exibir_media(4, 8)



if calcular_media(5, 10) < 6:
    print("Reprovado")
else:
    print("Aprovado")