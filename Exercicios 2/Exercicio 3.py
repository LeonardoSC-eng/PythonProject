horas = int(input("Digite as horas: "))
min = int(input("Digite os minutos: "))

if ((horas <0 or horas >23) and (min <0 or min >59)):
    print("Digite o valor correto de horas e minutos")
elif (horas <0 or horas >23):
    print("Digite o número das horas correta, entre 00h até 23h")
elif (min <0 or min >59):
    print("Digite o número correto dos minutos, entre 00 até 59 minutos")
else:
    print(f"São {horas}:{min}")