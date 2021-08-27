from os import replace
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice


class Senha:
    def __init__(self):
        self._caracteres_senha = {
            'maiuscula': [],
            'minuscula': [],
            'numero': [],
            'simbolo': []
        }
        self._sim = '!@#$%&*^?'
        self._senha = []
    
    def verifica_maiuscula(self, maiuscula):
        if maiuscula == True:
            self._caracteres_senha['maiuscula'].append(ascii_uppercase)
        else:
            self._caracteres_senha['maiuscula'].clear()

    def verifica_minuscula(self, minuscula):
        if minuscula == True:
            self._caracteres_senha['minuscula'].append(ascii_lowercase)
        else:
            self._caracteres_senha['minuscula'].clear()
    
    def verifica_numero(self, numero):
        if numero == True:
            self._caracteres_senha['numero'].append(digits)
        else:
            self._caracteres_senha['numero'].clear()
    
    def verifica_simbolo(self, simbolo):
        if simbolo == True:
            self._caracteres_senha['simbolo'].append(self._sim)
        else:
            self._caracteres_senha['simbolo'].clear()

    def _gerar_senha(self, tamanho):
        aux = []
        self._senha.clear()

        for valor in self._caracteres_senha.values():
            aux.append(str(valor).strip("[]"))

        aux = "".join(aux)
        aux = aux.replace("''", "").replace("'", "")

        for i in range(tamanho):
            self._senha.append(choice(aux))
        return "".join(self._senha)
