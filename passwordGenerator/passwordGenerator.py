import random
from wordGenerator import wordGenerator as word
from specialCharactersGenerator import specialCharactersGenerator as special
from digitsGenerator import digitsGenerator as digits

def gerarSenha(objTamanhos, qtdSenhas):

    tamSenha = objTamanhos['tamWord'] + objTamanhos['tamSpecial'] + objTamanhos['tamDigits']
    senha = []
    senhas = []

    for i in range(qtdSenhas):
        x = random.randint(1, 3)

        if x == 1:
            senha.append(str(word.wordGenerator(objTamanhos['tamWord']) + 
                special.specialCharactersGenerator(objTamanhos['tamSpecial']) + 
                digits.digitsGenerator(objTamanhos['tamDigits'])))
            print(f"Senha 1 {senha}")
        elif x == 2:
            senha.append(str(word.wordGenerator(objTamanhos['tamWord']) + 
                special.specialCharactersGenerator(objTamanhos['tamSpecial']) + 
                digits.digitsGenerator(objTamanhos['tamDigits'])))
            print(f"Senha 2 {senha}")
        else:
            senha.append(str(word.wordGenerator(objTamanhos['tamWord']) + 
                special.specialCharactersGenerator(objTamanhos['tamSpecial']) + 
                digits.digitsGenerator(objTamanhos['tamDigits'])))
            print(f"Senha 3 {senha}")

    

    # senhas = [ str(word.wordGenerator(objTamanhos['tamWord']) + 
    #     special.specialCharactersGenerator(objTamanhos['tamSpecial']) + 
    #     digits.digitsGenerator(objTamanhos['tamDigits']) )]