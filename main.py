from passwordGenerator import passwordGenerator as password


def imprimirMenu():
    print('''

        ======= Bem Vindo ao Gerador de Senhas =======

    ''')
    # print("")


def validações():

    tmSenha = 0

    while tmSenha < 1 or tmSenha > 3:
        print("Opções de tamanho de senha: ")
        print("1 - Senha Pequena(8 caracteres) ")
        print("2 - Senha Média(12 caracteres)")
        print("3 - Senha Grande(16 caracteres)")
        print("")

        tmSenha = int(input("Escolha uma das opções acima: "))

        if tmSenha < 1 or tmSenha > 3:

            print('Escolha apenas uma das opções acima!')
            print("")

    return tmSenha


op = ""

imprimirMenu()

while op.lower() != "n":

    qtdSenhas = int(input("Quantas senhas deseja gerar? "))
    print("")

    tamSenhas = validações()

    senhas = password.gerarSenha(tamSenhas, qtdSenhas)

    count = 1
    for i in senhas:
        print(f"{count}° Senha: {i}")
        count = count + 1

    op = str(input("\nDeseja gerar mais senhas?\nResponda com (S/N)"))

print("Tchau, tenha um bom dia! :)")
        
