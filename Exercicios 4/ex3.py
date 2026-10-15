total = 0

while True:
    valor = int(input("Digite um valor ou digite 0 para somar: "))
    if valor == 0:
        print(f"O valor total é de: {total}")
        break
    else:
        total = total + valor