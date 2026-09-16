idade = int(input("Digite sua Idade: "))
cnh = input("Tem CNH? (sim ou nao): ")

if (idade >= 18 and cnh == "sim"):
    print("Você é permitido a dirigir")
else:
    print("Você não em idade para dirigir")