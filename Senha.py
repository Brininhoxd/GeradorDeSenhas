from string import ascii_lowercase, ascii_uppercase, digits


config_senha = {
    'maiuscula': False,
    'minuscula': False,
    'numero': False,
    'simbolos': False
}

class Senha:
    def __init__(self, config_senha):
        self._config_senha = config_senha
        self._senha = []
        self._sim = '!@#$%&*^?'
    
    def verificaConfigSenha(self, mai, min, num, sim):
        self._config_senha['maiuscula'] = True if mai else self._config_senha['maiuscula'] = False
        self._config_senha['minuscula'] = True if min else self._config_senha['minuscula'] = False
        self._config_senha['numero'] = True if num else self._config_senha['numero'] = False
        self._config_senha['simbolos'] = True if sim else self._config_senha['simbolos'] = False

    def montarConfigSenha(self):
        if self._config_senha['maiuscula'] == True:
            self._senha.append(ascii_uppercase)
        if self._config_senha['minuscula'] == True:
            self._senha.append(ascii_lowercase)
        if self._config_senha['numero'] == True:
            self._senha.append(digits)
        if self._config_senha['simbolos'] == True:
            self._senha.append(self._sim.split())

        


        


    


