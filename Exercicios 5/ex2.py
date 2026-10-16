valor = float(input("Digite um valor em reais: R$"))
moeda = input("Digite a sigla da moeda estrangeira (USD | EUR | GBP): ").upper()

match moeda:
    case "USD":
        valor = valor * 0.20
    case "EUR":
        valor = valor * 0.18
    case "GBP":
        valor = valor * 0.15
    case _:
        print("Moeda não suportada")
print(f"O valor convertido fica {moeda}{valor}")