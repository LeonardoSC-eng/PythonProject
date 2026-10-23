def calcular_preco_final(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto


preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto (%): "))

preco_final = calcular_preco_final(preco, percentual)
valor_descontado = preco - preco_final

print(f"Preço original: R$ {preco}")
print(f"Valor descontado: R$ {valor_descontado}")
print(f"Preço final: R$ {preco_final}")