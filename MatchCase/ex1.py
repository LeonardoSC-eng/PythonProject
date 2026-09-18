opcao = int(input("Digite uma opção (0 até 3): "))

# A estrutura match-case por padrão compara valores por igualdade
# Em outras linguagens é conhecido como SWITCH-CASE
# No Match informamos a variavel que será verificada, no nosso caso é "opcao"
# No Match não há limitação para cases, podemos te N
# Porém, de maneira mínima há 1 CASE e 1 CASE Default (case _:)

match opcao:
    case 0:
        print("Opção 0")
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Valor incorreto. Digite de 0 até 3")

# Ou

if opcao == 0:
    print("Opção 0")
elif opcao == 1:
    print("Opção 1")
elif opcao == 2:
    print("Opção 2")
elif opcao == 3:
    print("Opção 3")
else:
    print("Valor incorreto. Digite de 0 até 3")