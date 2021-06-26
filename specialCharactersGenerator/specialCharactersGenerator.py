
## * Arquivo onde será gerado os caracteres especiais

import random

def specialCharactersGenerator(tamanho):
    caracteres = "!#$%&+-/<=>?@\_"
    arrayCaracteres = list(caracteres)

    caracteresGerados = []

    for i in range(tamanho):

        caracteresGerados.append(random.choice(arrayCaracteres))

    return "".join(caracteresGerados)