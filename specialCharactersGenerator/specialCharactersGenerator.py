
## * Arquivo onde será gerado os caracteres especiais

import random
import string

caracteres = "!#$%&+-/<=>?@\_"
digitos = string.digits
arrayCaracteres = list(caracteres)

caracteresGerados = []

def specialCharactersGenerator(tamanho):
    for i in range(tamanho):
        # x = random.randint(1, len(arrayCaracteres))

        caracteresGerados.append(random.choice(arrayCaracteres))

    return "".join(caracteresGerados)