num1 = int(input("Digite as horas: "))
num2 = int(input("Digite os minutos: "))

if (num1 > 23 or num1 < 0) and (num2 > 59 or num2 < 0):
    print("Número das horas e dos minutos incorreto, digite um número correto para horas e minutos")
elif num1 > 23 or num1 < 0:
    print("Número das horas incorreto, digite um numero de 0 a 23")
elif num2 > 59 or num2 < 0:
    print("Número dos minutos incorreto, digite um numero de 0 a 59")
else:
    print(f"O horário digitado foi {num1}:{num2}")