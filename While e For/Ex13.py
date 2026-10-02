#Gerenciar Aluno
#1 - Cadastrar
#2 - Consultar
#3 - Atualizar
#4 - Remover
#5 - Listar Alunos
#6 - Sair do programa

#Vou usar MatchCase ao inves de IfElse

while True:
    print("GERENCIAR ALUNO")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Listar Alunos")
    print("6 - Sair do programa")
    opcao = input("Digite uma opcao: ")

    #Função isdigit: confere se a variavel tem digitos de 0 a 9, e não é outro caractere ou está vazio
    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            print("Cadastrando Aluno\n")
        elif opcao == 2:
            print("Consultando Aluno\n")
        elif opcao == 3:
            print("Atualizando Aluno\n")
        elif opcao == 4:
            print("Remover o Aluno\n")
        elif opcao == 5:
            print("Listar os Alunos\n")
        elif opcao == 6:
            print("Sair do Programa\n")
            break
        else:
            print("Opcao invalida, tente novamente\n")
    else:
        print("Opcao invalida, digite um número ao invés de uma letra\n")