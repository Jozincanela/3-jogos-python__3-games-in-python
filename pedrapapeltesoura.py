# Desafio 2:

# Vamos construir um jogo de "Pedra, papel, tesoura"!
# Um jogador humano irá disputar contra a máquina.
# Esse jogador deverá escolher entre "pedra", "papel" ou "tesoura" como manobras válidas.
# Caso a escolha do jogador seja inválida, o jogo em si não deve acontecer
# e uma mensagem de erro "Jogada inválida" deve ser exibida.
# 
# O Computador deve escolher entre "pedra", "papel" ou "tesoura" de forma aleatória.
# E só relembrando: papel vence tesoura, tesoura vence papel, papel vence pedra.
# Se a jogada for válida o programa deve definir quem foi o vencedor
# E exibir qual jogada cada jogador escolheu e quem foi o vencedor.
decisao =0
while decisao == 0:
    print("bem vindo ao pedra papel tesoura")
    escolha = int(input("1-pedra, 2-papel, 3-tesoura"))
    escolhas = ["nada" , "pedra", "papel", "tesoura"]
    from random import randint
    escolha_bot = randint(1,3)
    vitoriasbot= 0
    vitoriasusu= 0
    if escolha == 1 and escolha_bot == 2 :
        print(f"você perdeu porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasbot += 1
    elif escolha == 2 and escolha_bot == 1:
        print(f"você ganhou porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasusu += 1
    elif escolha == 1 and escolha_bot == 3:
        print(f"você ganhou porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasusu += 1
    elif escolha == 3 and escolha_bot == 1:
        print(f"você perdeu porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasbot += 1
    elif escolha == 3  and escolha_bot == 2:
        print(f"você ganhou porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasusu += 1
    elif escolha == 2 and escolha_bot == 3:
        print(f"você perdeu porque o computador escolheu {escolhas[escolha_bot]} e você escolheu {escolhas[escolha]}")
        vitoriasbot += 1
    elif escolha == escolha_bot:
        print("você e o computador escolheram a mesma coisa")
    elif escolha > 3 or escolha < 0 :
        print("escolha invalida")
    
    decisao = int(input("deseja continuar a jogar? 0-sim, 1-não"))

if vitoriasusu > vitoriasbot:
    print(f"de acordo com todas as partidas você foi campeão em cima do computador com {vitoriasusu} vitorias e o computador com {vitoriasbot}")  
elif vitoriasusu < vitoriasbot:
    print(f"de acordo com todas as partidas você foi o perderdor em cima do computador com {vitoriasusu} vitorias e o computador com {vitoriasbot}") 
else:
    print("você empatou com o computador")
