def exibir_menu():
    print("\n------ MENU ---------")
    print("1 – Realizar nova simulação")
    print("2 – Consultar contratos realizados")
    print("3 – Encerrar sistema")


def consultar_contratos(total_contratos, valor_acumulado):
    print(f"\nQuantidade de contratos simulados: {total_contratos}")
    print(f"Valor total financiado acumulado: R${valor_acumulado}")



def calcular_evolucao_saldo(valor_emprestimo, taxa_juros, meses):
    print()
    saldo_atual = valor_emprestimo
    taxa_decimal = taxa_juros / 100

    for mes in range(1, meses + 1):
        saldo_atual = saldo_atual * (1 + taxa_decimal)
        print(f"Mês {mes}: R${saldo_atual}")

    valor_total_financiado = saldo_atual
    valor_parcela = valor_total_financiado / meses

    return valor_total_financiado, valor_parcela

quantidade_simulados = 0
total_financiado_acumulado = 0.0

while True:
    exibir_menu()
    opcao = input("\nDigite uma opção: ")

    if opcao == '1':
        valor_emp = float(input("Digite o valor do empréstimo R$: "))
        taxa = float(input("Digite a taxa de juros (%): "))
        qtd_meses = int(input("Digite a quantidade de meses: "))

        total_financiado, parcela = calcular_evolucao_saldo(valor_emp, taxa, qtd_meses)

        print(f"\nValor total financiado: R${total_financiado}")
        print(f"Valor de cada parcela: R${parcela}")

        quantidade_simulados += 1
        total_financiado_acumulado += total_financiado

    elif opcao == '2':
        consultar_contratos(quantidade_simulados, total_financiado_acumulado)

    elif opcao == '3':
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
