dia = int(input("Digite um dia (1 até 7): "))

match dia:
    case 0:
        print("Domingo")
    case 1:
        print("Segunda")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4:
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sabado")
    case _:
        print("Valor incorreto. Digite de 0 até 7")