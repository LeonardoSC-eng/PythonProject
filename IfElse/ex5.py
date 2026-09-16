senha = input("Digie a senha: ")
usuario = input("Digite seu usuario: ")
if (senha == "fiap" and usuario == "admin"):
    print("Acesso permitido")
else:
    print("Senha incorreta")

if (senha != "fiap" or usuario != "admin"):
    print("Senha incorreta")
else:
    print("Acesso permitido")