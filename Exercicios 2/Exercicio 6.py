salario = float(input("Digite seu salário: R$"))
vendas = float(input("Digite o valor das suas vendas: R$"))
comissao = 0.0

if (vendas <= 5000):
    comissao = vendas * 0.05
else:
    excedente = vendas - 5000
    comissao = (5000 * 0.05) + (excedente * 0.07)

print(f"Sua comissão é de R$ {comissao}")
print(f"Seu salario total é de R$ {salario + comissao}")