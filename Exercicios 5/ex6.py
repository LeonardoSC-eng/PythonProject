valorTotal = 0.0
while True:
    prato = int(input("---------x---------\n"
                     "CARDAPIO\n"
                     "1 - Hamburguer - R$40,00\n"
                     "2 - Lasanha - R$60,00\n"
                     "3 - Bife acebolado - R$30,00\n"
                     "4 - Strogonoff - R$35,00\n"
                     "5 - Picanha - R$60,00\n"
                     "6 - Churrasco - R$60,00\n"
                     "7 - Fechar conta\n"
                     "Digite um número do menu: "))
    match prato:
        case 1:
            print("Hamburguer adicionado na conta!!!")
            valorTotal = valorTotal + 40
        case 2:
            print("Lasanha adicionado na conta!!!")
            valorTotal = valorTotal + 60
        case 3:
            print("Bife adicionado na conta!!!")
            valorTotal = valorTotal + 30
        case 4:
            print("Strogonoff adicionado na conta!!!")
            valorTotal = valorTotal + 35
        case 5:
            print("Picanha adicionado na conta!!!")
            valorTotal = valorTotal + 60
        case 6:
            print("Churrasco adicionado na conta!!!")
            valorTotal = valorTotal + 60
        case 7:
            while True:
                taxa = input("Deseja incluir a taxa de serviços? (Sim ou Não): ").lower()
                match taxa:
                    case "sim":
                        valorTotal = valorTotal * 1.10
                        print("Taxa adicionada na conta!!!")
                        break
                    case "nao" | "não":
                        print("Taxa não adicionada na conta!!!")
                        break
                    case _:
                        print("Digite apenas Sim ou Não")
            print(f"O valor total da conta é de R${valorTotal}")
            break
        case _:
            print("Número incorreto, digite o número correto do menu (1 a 7)")