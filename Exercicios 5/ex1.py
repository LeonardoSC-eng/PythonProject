dia = input("Escreva um dia da semana (ex: Segunda): ").lower()

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sabado" | "domingo":
        print("Fim de semana")
    case _:
        print("Incorreto, digite um dia da semana sem acentos")