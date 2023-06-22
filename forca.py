# Desafio 3

# Criar um jogo da Forca.
# Utilizando a lista de frutas, criaremos um jogo da Forca.
# O Computador deve escolher uma palavra secreta da lista.
# O jogador deve tentar adivnhar letra por letra.
# O número máximo de tentativas é 6. 
# A palavra deve ser exibida parcialmente na medida em que o jogador vai acertando.
# Ex: se a palavra secreta for morango e tentaram a letra 'o':
# deve ser exibido:  _ o _ _ _ _ o
# O jogador não deve perder tentativas ao tentar repetir uma letra, mas deve ser avisado
# que já tentou aquela letra.
# O número de tentativas deve ser exibido a cada vez que o jogador falha!!!
# Quando chegar a 0 tentativas o jogador mor... perde...
# Caso consiga advinhar a palavra, uma mensagem deve ser exibida para comemorar
# a gloriosa e improvável vitória de nosso jogador.

def palavra_aleatoria () -> str : 
    from random import randint
    numero_magico = randint(0,42)
    lista_frutas = ["abacate","amora","ameixa","acerola","abacaxi","acai","banana","carambola","caju","cereja","cacau","caqui","cupuaçu","damasco","figo","framboesa","graviola","goiaba","groselia","guarana","jaca","kiwi","laranja","limao","lima","lixia","melancia","mamao","melao","maracuja","manga","maca","mexerica","morango","nectarina","pera","pessego","pitanga","pinha","quina","roma","tangerina","uva"]
    palavra  = lista_frutas[numero_magico] 
    return palavra

  
def tamanho_palavra (palavra) -> int :
  return len (palavra)


def lista_letras_palavras (palavra) -> list :
  letras = list(palavra)
  return letras

def tentativa (lista_palavra, letras ) -> str:
    tentativas_acerto = ""
    for letra in lista_palavra:
        for caracter in letras: 
            if caracter == letra:
                tentativas_acerto += caracter
                break 
        if caracter == letra:
            78+5
        elif caracter != letra:
             tentativas_acerto += "_"

    return tentativas_acerto
    

    
    




palavra = palavra_aleatoria()   
tamanho = tamanho_palavra(palavra)
lista_letras = lista_letras_palavras(palavra)
letras = []
palavra_secreta= ""
for i in range(0, tamanho) :
    palavra_secreta += "_"


print(palavra_secreta)
tamanho = tamanho_palavra(palavra)
x = 6

letra = input("digite uma letra: ")
letras.append(letra)
tentativa(lista_letras,letras)
print(tentativa(lista_letras,letras))
tentativa_ss = tentativa(lista_letras,letras)
if palavra_secreta ==  tentativa_ss: 
    x -= 1
print(f"você tem {x} tentativas")

while x != 0:
    tentativa_falha =  tentativa(lista_letras,letras)

    letra = input("digite uma letra: ")
    letras.append(letra)
    tentativa(lista_letras,letras)
    print(tentativa(lista_letras,letras))
    tentativa_ss = tentativa(lista_letras,letras)
    if tentativa_falha ==  tentativa_ss:
        x -= 1
    
    
    
    if tentativa_ss == palavra:
        print(f"\033[34mparabens você ganhou a forca!!! \33[m")
        break
    print(f"você tem {x} tentativas")
    

if x == 0 :
    print("você perdeu a forca")
    
    
    
    


    




        


    
                   
        


            
                
        
        
        
     
            
    
        


    



        

                
                
   
        
        
    
    
    

