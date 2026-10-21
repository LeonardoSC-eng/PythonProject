def validar_senha(senha):
    if senha == "Senha123":
        return True
    else:
        return False

while True:
    x = input("Digite uma senha: ")
    if validar_senha(x) == True:
        print("Senha valida!")
        break
    else:
        print("Senha invalida!")
        continue