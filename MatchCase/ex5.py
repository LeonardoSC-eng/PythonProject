idade = int(input("Digite a sua idade: "))

# x é o valor que vem da variavel idade
# foi definido uma variavel genérica para informar um valor possivel

match idade:
    case x if x >= 18:
        print("Maior de idade")
    case x if x <18:
        print("Menor de idade")
    case _:
        print("Valor inválido")