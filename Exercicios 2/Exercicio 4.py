num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if (num1 > num2):
    print(f"O maior número entre eles é o {num1}")
elif (num2 > num1):
    print(f"O maior número entre eles é o {num2}")
else:
    print("Os números são iguais")