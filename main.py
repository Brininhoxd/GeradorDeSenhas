from passwordGenerator import passwordGenerator as password


def imprimirMenu():
    print("Menu")
    print("")


def validações():

    tmSenha = 0

    while tmSenha < 1 or tmSenha > 3:
        print("Opções de tamanho de senha: ")
        print("1 - Senha Pequena(8 caracteres) ")
        print("2 - Senha Média(16 caracteres)")
        print("3 - Senha Grande(24 caracteres)")
        print("")

        tmSenha = int(input("Escolha uma das opções acima: "))

        if tmSenha < 1 or tmSenha > 3:

            print('Escolha apenas uma das opções acima!')
            print("")

    return tmSenha


op = ""

while op.lower() != "s":
    imprimirMenu()

    qtdSenhas = int(input("Quantas senhas deseja gerar? "))
    print("")

    tamSenhas = validações()

    senhas = password.gerarSenha(tamSenhas, qtdSenhas)

    print(senhas)
