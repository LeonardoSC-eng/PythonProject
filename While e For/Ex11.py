while True:
    n = int(input("Digite 0 ou 1 para sair "))

    if n == 0 or n == 1:
        print(f"Você digitou {n} para sair")
        break

    print("Você digitou", n)

print("Fora do Laço!")