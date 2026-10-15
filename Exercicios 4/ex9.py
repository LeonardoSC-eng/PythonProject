salario = float(input("Digite seu salario: "))
ajuste = float(input("Digite o percentual de aumento: "))

print(f"Seu salário é de: R${salario}\n"
      f"O reajuste é de {ajuste}%\n"
      f"Seu aumento: R${((salario * ajuste) / 100) + salario}")
