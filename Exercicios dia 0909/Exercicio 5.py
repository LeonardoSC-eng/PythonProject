nome = input("Digite seu nome: ")
qntprod = float(input("Digite a quantidade de produtos vendidos: "))
totalven = float(input("Digite o valor total das vendas: "))

salario = float(1800)
comissao = float(150)

print(f"{nome}, o valor total do seu salário é de: {(comissao * qntprod)+((totalven/100)*3)+salario}")