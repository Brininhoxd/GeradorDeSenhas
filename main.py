from passwordGenerator import passwordGenerator as password


def imprimirMenu():
    print("Menu")
    print("")

def validações():

    tmSenha = 0

    while tmSenha < 8 or tmSenha > 24:
        tmSenha = int(input("Quantos caracteres deseja na sua senha? "))
        print("")

        if tmSenha < 8 or tmSenha > 24:
            
            print('Obs: Digite uma quantidade de caracteres entre "8" e "24". \nPara que seja segura e fácil de lembrar! ')
            print("")

    tamWord = tmSenha - 4
    tamSpecial = 2
    tamDigits = 2

    Tamanhos = { 'tamWord': tamWord,
                    'tamSpecial': tamSpecial,
                    'tamDigits': tamDigits}

    return Tamanhos

op = ""

while op.lower() != "s":
    imprimirMenu()

    qtdSenhas = int(input("Quantas senhas deseja gerar? "))
    print("")

    objTamanhos = validações()

    password.gerarSenha(objTamanhos, qtdSenhas)
    
    
    
