import random
import datetime
from wordGenerator import wordGenerator as word
from specialCharactersGenerator import specialCharactersGenerator as special
from digitsGenerator import digitsGenerator as digits


def ValidaSenha(op):
    if op == 1:
        tamWord = 3
        tamDigits = 1
        tamSpecial = 1
        tempSenha = []

        tempSenha.append(str(special.specialCharactersGenerator(tamSpecial) +  # * 1
                             digits.digitsGenerator(tamDigits) +  # * 1
                             word.wordGenerator(tamWord) +  # * 3
                             digits.digitsGenerator(tamDigits) +  # * 1
                             special.specialCharactersGenerator(tamSpecial)))  # * 1

        return "".join(tempSenha)
    if op == 2:
        tamWord = 3
        tamDigits = 4
        tamSpecial = 1
        tempSenha = []

        tempSenha.append(str(special.specialCharactersGenerator(tamSpecial) +  # * 1
                             word.wordGenerator(tamWord) +  # * 3
                             str(random.randint(1700, datetime.date.today().year)) +
                             word.wordGenerator(tamWord) +  # * 3
                             special.specialCharactersGenerator(tamSpecial)))  # * 1

        return "".join(tempSenha)
    if op == 3:
        tamWord = 4
        tamDigits = 2
        tamSpecial = 1
        tempSenha = []

        tempSenha.append(str(special.specialCharactersGenerator(tamSpecial) +  # * 1
                             word.wordGenerator(tamWord) +  # * 4
                             digits.digitsGenerator(tamDigits) +  # * 2
                             # * 1
                             special.specialCharactersGenerator(tamSpecial) +
                             digits.digitsGenerator(tamDigits) +  # * 2
                             word.wordGenerator(tamWord) +  # * 4
                             special.specialCharactersGenerator(tamSpecial)))  # * 1

        return "".join(tempSenha)


def gerarSenha(tamSenhas, qtdSenhas):
    senhas = []
    senha = ""
    # x = len(senha.)

    if tamSenhas == 1:
        # * 8 caracteres
        for i in range(qtdSenhas):
            while len(senha) != 8:
                senha = ValidaSenha(tamSenhas)

            senhas.append("".join(senha))
            senha = ""
        return senhas

    elif tamSenhas == 2:
        # * 12 caracteres
        for i in range(qtdSenhas):
            while len(senha) != 12:
                senha = ValidaSenha(tamSenhas)

            senhas.append("".join(senha))
            senha = ""
        return senhas

    elif tamSenhas == 3:
        # * 16 caracteres
        for i in range(qtdSenhas):
            while len(senha) != 16:
                senha = ValidaSenha(tamSenhas)

            senhas.append("".join(senha))
            senha = ""
        return senhas
