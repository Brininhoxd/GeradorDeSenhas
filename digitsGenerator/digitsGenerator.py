
## * Arquivo onde será gerado os digitos

import random
import string

digitos = list(string.digits)

caracteresGerados = []

def digitsGenerator(tamanho):
    for i in range(tamanho):

        caracteresGerados.append(random.choice(digitos))

    return "".join(caracteresGerados)

print (digitsGenerator(5))