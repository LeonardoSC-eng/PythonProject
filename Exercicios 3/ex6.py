salfixo = float(input("Digite seu salário: "))
vendas = float(input("Digite o valor das vendas: "))
comi = 0.0

if salfixo <= 0 or vendas < 0:
    print("Valor incorreto")
elif vendas > 5000:
    comi = vendas * 0.07
    print(f"Seu salário é R${salfixo}\n"
          f"Sua comissão é R${comi}\n"
          f"O total do seu pagamento é R${salfixo + comi}")
else:
    comi = vendas * 0.05
    print(f"Seu salário é R${salfixo}\n"
          f"Sua comissão é R${comi}\n"
          f"O total do seu pagamento é R${salfixo + comi}")
