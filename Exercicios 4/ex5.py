while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 == num2:
        print("Digite números diferentes")
    else:
        print(f"A soma entre os 2 números é de {num1+num2}")
        break