from asyncio import print_call_graph

senha = input("Digie a senha: ")
if (senha != "fiap"):
    print("Senha incorreta")
else:
    print("Acesso permitido")