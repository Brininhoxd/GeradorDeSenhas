from wordGenerator import wordGenerator as word
from specialCharactersGenerator import specialCharactersGenerator as special

palavra = str(word.wordGenerator(4) + special.specialCharactersGenerator(4))

print(palavra)