num = int(input("Digite um número para calcular: "))
cal =int(input("Digite um número do menu para calcular\n"
                 "1 - Dobro do número\n"
                 "2 - Metade do número\n"
                 "3 - 10% do número\n"))
match cal:
    case 1:
        num = num * 2
        print(f"O resultado do calculo é: {num}")
    case 2:
        num = num / 2
        print(f"O resultado do calculo é: {num}")
    case 3:
        num = num * 0.10
        print(f"O resultado do calculo é: {num}")
    case _:
        print("Número do menu invalido, digite um número correto de 1 a 3")