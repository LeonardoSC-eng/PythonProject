qnt = 0

for i in range(1, 15):
    num = int(input(f"Digite o {i}° número: "))
    if num <= 50 and num >= 10:
        qnt += 1
print(f"A quantidade de números entre 10 e 50 é de {qnt}")