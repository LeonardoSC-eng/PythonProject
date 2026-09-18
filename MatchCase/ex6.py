idade = int(input("Digite sua idade: "))
cnh = input("Tem CNH? (sim ou nao): ").lower()

#i é a idade
#c é a cnh

match idade,cnh:
    #sem a nova variavel
    case i, "sim" if i>=18:
        print("Permitido a dirigir")
    #com variaveis novas
    case i,c if i<18 and c=="nao":
        print("Não é permitido a dirigir")
    case i,c if i>=18 and c=="nao":
        print("Tem idade para tirar CNH, mas não pode dirigir")
    #com a segunda variavel vazia
    case i, _ if i<0:
        print("idade invalida")
    case _:
        print("Valores invalidos")