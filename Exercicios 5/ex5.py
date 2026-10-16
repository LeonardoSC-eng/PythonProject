while True:
    operacao = int(input("---------x---------\n"
                         "MENU DE OPERAÇÕES\n"
                         "1 - Check-in\n"
                         "2 - Check-out\n"
                         "3 - Consultar Quarto\n"
                         "4 - Sair\n"
                         "Digite um número do menu: "))
    match operacao:
        case 1:
            print("Check-in feito as 14:00")
        case 2:
            print("Check-out feito as 11:00")
        case 3:
            print("Quarto 702, andar 7")
        case 4:
            print("OPERAÇÃO FINALIZADA")
            break
        case _:
            print("Número invalido, digite um número de 1 a 4")