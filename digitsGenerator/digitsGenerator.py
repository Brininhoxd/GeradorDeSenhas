
# * Arquivo onde será gerado os digitos

import random
import string


def digitsGenerator(tamanho):

    digitos = list(string.digits)

    caracteresGerados = []
    for i in range(tamanho):

        caracteresGerados.append(random.choice(digitos))

    return "".join(caracteresGerados)
