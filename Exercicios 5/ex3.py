mes = input("Escreva um mês (Ex: Janeiro, Fevereiro...): ").lower()

match mes:
    case "dezembro" | "janeiro" | "fevereiro":
        print("Verão")
    case "março" | "abril" | "maio":
        print("Outono")
    case "junho" | "julho" | "agosto":
        print("Inverno")
    case "setembro" | "outubro" | "novembro":
        print("Primavera")
    case _:
        print("Incorreto, digite um mês do ano (Ex: Fevereiro, Março...)")