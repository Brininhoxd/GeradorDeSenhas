
## * Arquivo onde será gerado as palavras

import random

def wordGenerator(tamanho):
    arrayAey = ["a","e","i","o"]
    arrayLh = ["lh","nh","ch"]
    arrayBcd = ["b","c","d","f","g","j","k","l","m","n","p","r","s","t","v","x","z"]
    arrayQu = ["qua","qui","quo","que"]
    arrayLms = ["l","m","s","r"]

    palavra = []

    for i in range(tamanho):
        x = random.randint(1, 5)

        if x == 1:
            if ((tamanho - 1) - i) < 2:
                palavra.append(random.choice(arrayLms))            
            else:
                palavra.append(random.choice(arrayLms))
                i =+ 1
                palavra.append(random.choice(arrayAey))            

        elif x == 2:
            palavra.append(random.choice(arrayAey))        

        elif x == 3:
            if((tamanho - 1) - i) < 3:
                if ((tamanho - 1) - i) < 2:
                    palavra.append(random.choice(arrayLms))                
                else:
                    palavra.append(random.choice(arrayBcd))
                    i =+ 1
                    palavra.append(random.choice(arrayAey))                
            else:
                palavra.append(random.choice(arrayLh))
                i =+ 1
                palavra.append(random.choice(arrayAey))            

        elif x == 4:
            if ((tamanho - 1) - i) < 2:
                palavra.append(random.choice(arrayLms))            
            else:
                palavra.append(random.choice(arrayBcd))
                i =+ 1
                palavra.append(random.choice(arrayAey))            
        
        elif x == 5:
            if((tamanho - 1) - i) < 3:
                if ((tamanho - 1) - i) < 2:
                    palavra.append(random.choice(arrayLms))                
                else:
                    palavra.append(random.choice(arrayBcd))
                    i =+ 1                  
            else:
                palavra.append(random.choice(arrayQu))
                i =+ 1 
    
    palavraString = "".join(palavra)

    return palavraString
        
        
