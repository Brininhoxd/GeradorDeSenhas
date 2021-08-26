from string import ascii_lowercase, ascii_uppercase, digits
from random import choice


config_senha = {
    'maiuscula': False,
    'minuscula': False,
    'numero': False,
    'simbolo': False
}

class Senha:
    def __init__(self):
        self._config_senha = config_senha
        self._caracteres_senha = []
        self._sim = '!@#$%&*^?'
        self._senha = []
    
    def verifica_maiuscula(self, maiuscula):
        if maiuscula:
            self._config_senha['maiuscula'] = True
        else:
            self._config_senha['maiuscula'] = False

    def verifica_minuscula(self, minuscula):
        if minuscula:
            self._config_senha['minuscula'] = True
        else:
            self._config_senha['minuscula'] = False
    
    def verifica_numero(self, numero):
        if numero:
            self._config_senha['numero'] = True
        else:
            self._config_senha['numero'] = False
    
    def verifica_simbolo(self, simbolo):
        if simbolo:
            self._config_senha['simbolo'] = True
        else:
            self._config_senha['simbolo'] = False


    def montar_config_senha(self, tamanho):
        if self._config_senha['maiuscula'] == True:
            self._caracteres_senha.append(ascii_uppercase)
        if self._config_senha['minuscula'] == True:
            self._caracteres_senha.append(ascii_lowercase)
        if self._config_senha['numero'] == True:
            self._caracteres_senha.append(digits)
        if self._config_senha['simbolo'] == True:
            self._caracteres_senha.append(self._sim.split())
        
        return self._gerar_senha(tamanho)

    def _gerar_senha(self, tamanho):
        for i in range(tamanho):
            self._senha.append(choice(self._caracteres_senha))
        return "".join(self._senha)
