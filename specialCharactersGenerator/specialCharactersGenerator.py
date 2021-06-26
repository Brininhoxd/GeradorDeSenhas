
## * Arquivo onde será gerado os caracteres especiais

import random

caracteres = "!#$%&+-/<=>?@\_"
arrayCaracteres = list(caracteres)

caracteresGerados = []

def specialCharactersGenerator(tamanho):
    for i in range(tamanho):

        caracteresGerados.append(random.choice(arrayCaracteres))

    return "".join(caracteresGerados)