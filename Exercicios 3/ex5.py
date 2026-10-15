num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo: "))
num3 = int(input("Digite o terceiro: "))

if num1 < num2 and num1 < num3:
    print(f"O menor número é {num1}")
elif num2 < num3 and num2 < num1:
    print(f"O menor número é {num2}")
elif num3 < num2 and num3 < num1:
    print(f"O menor número é {num3}")
else:
    print(f"Números iguais")