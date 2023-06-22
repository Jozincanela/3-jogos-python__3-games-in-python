# Desafio 1:

# Vamos criar um jogo de advinhação.
# O Computador irá escolher de forma aleatória um número entre 1 e 100.
# O jogador deve tentar adivnhar o número
# Apenas valores numéricos são válidos.
from random import randint
numero_magico = randint(0,100)
numero = input("qual o numero magico?")
xx=1

while xx > 0:
    if numero.isnumeric() == False or (int(numero)> 100 and int(numero) > 0) :
        print("o que você digitou é maior que 100 ou menor que 0 ou é uma palavra ")
        while   numero.isnumeric() == False or (int(numero)> 100 and int(numero) > 0)  :
                numero = input("digite novamente!")

       
    numero_escolhido = int(numero)
    
    if numero_escolhido != numero_magico :
        
        if numero_escolhido > numero_magico:
            print("o numero que você digitou é maior que o numero magico")
            
            numero = input("digite novamente!")
        else :
             print("o numero que você digitou é menor que o numero magico")
             numero = input("digite novamente!")
    elif numero_escolhido == numero_magico:
        break
    
print("Parabens você adivinhou o numero magico!!!")