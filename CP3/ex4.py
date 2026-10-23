faturamento_total = 0.0
tipo_atual = 0


def mostrar_menu():
    print("\n------ MENU --------")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Ver faturamento")
    print("4 - Encerrar")


def preco_hora(tipo):
    if tipo == 1:
        return 8.00
    elif tipo == 2:
        return 5.00
    elif tipo == 3:
        return 12.00
    else:
        return 0.0


def registrar_entrada():
    global tipo_atual

    placa = input("\nDigite a placa: ")
    print("1 - Carro | 2 - Moto | 3 - Caminhonete")
    tipo = int(input("Digite o tipo do veículo: "))

    if tipo < 1 or tipo > 3:
        print("Tipo de veículo inválido.")
        return

    tipo_atual = tipo
    print("\nEntrada registrada com sucesso.")


def calcular_desconto(horas, subtotal):
    if horas <= 2:
        return 0.0
    elif horas <= 5:
        return subtotal * 0.05
    else:
        return subtotal * 0.10


def registrar_saida():
    global faturamento_total, tipo_atual

    if tipo_atual == 0:
        print("\nNenhum veículo registrado na entrada.")
        return

    horas = int(input("\nDigite a quantidade de horas: "))

    if horas <= 0:
        print("Quantidade de horas inválida.")
        return

    subtotal = horas * preco_hora(tipo_atual)
    desconto = calcular_desconto(horas, subtotal)
    total = subtotal - desconto

    faturamento_total += total
    tipo_atual = 0

    print(f"\nSubtotal da estadia R$ {subtotal}")
    print(f"Desconto aplicado R$ {desconto}")
    print(f"Total a pagar R$ {total}")


def ver_faturamento():
    print(f"\nFaturamento acumulado do dia: R$ {faturamento_total}")


def main():
    opcao = 0

    while opcao != 4:
        mostrar_menu()
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            registrar_entrada()
        elif opcao == 2:
            registrar_saida()
        elif opcao == 3:
            ver_faturamento()
        elif opcao == 4:
            print(f"\nPrograma encerrado. Faturamento total: R$ {faturamento_total}")
        else:
            print("Opção inválida.")


main()