dia = input("Digite o dia da semana: ").lower()

#função lower: Transformar texto em minusculo

match dia:
    case "segunda" | "Terça" | "quarta" | "quinta" | "sexta":
        print("Dia util")
    case "sabado" | "domingo":
        print("Final de semana")