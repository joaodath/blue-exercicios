# Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# Permitir que eu decida quantas rodadas iremos fazer; x
# Rodar o código durante as rodadas 
# Ler a minha escolha (Pedra, papel ou tesoura); x
# Decidir de forma aleatória a decisão do computador; x
# Mostrar quantas rodadas cada jogador ganhou; x
# Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador); x
# Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa. x
#Vamos limpar as coisas por aqui?
import os
#Limpando a tela do Interpretador no Windows
clear = lambda: os.system('cls')
clear()
#Limpando a tela do Interpretador no Linux
clear = lambda: os.system('clear')
clear()
#Okay, agora podemos continuar :)
#Início do Código do Projeto
from time import sleep
from random import randint
rodadas = cont_rodadas = empate = pc = usuario = 0
opcao = ' '
opcaoPC = ' '
quer_continuar = True
sleep(1)
while quer_continuar == True:
    rodadas = int(input('Quantas rodadas iremos jogar? '))
#Bloco para Fazer a Escolha do Computador
    for i in range(rodadas):
        jokenpo = randint(1,3)
        if jokenpo == 1:
            opcaoPC = 'pedra'
        elif jokenpo == 2:
            opcaoPC = 'papel'
        else:
            opcaoPC = 'tesoura'
    #print(f'Eu escolhi {opcaoPC}.') #opção de debug
    #Fim do Bloco para Fazer a Escolha do Computador
        sleep(1)
        print('''
        Okay, estou pronto!
        Já escolhi minha opção. E você?''')
        print()
        sleep(1)
        opcao = str(input('Você escolhe Pedra, Papel ou Tesoura? ')).strip().lower()
        sleep(1)
        print()
        if opcao == 'pedra' or opcao == 'papel' or opcao == 'tesoura':
            cont_rodadas += 1
            print(f'Você escolheu {opcao}. Quem será que ganhou?')
        else:
            print('Você não sabe brincar! :(')
            break
        sleep(1)
    #Inicio do bloco do jogo. 
        # Aqui o computador calcula as pontuações e imprime quem venceu a partida atual. Ele também vai somar +1 nas variáveis de contagem de empate, vitória do pc e vitória do usuário.
        if opcao == 'pedra' and opcaoPC == 'pedra':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Temos um empate!''')
            print()
            empate += 1
        elif opcao == 'papel' and opcaoPC == 'papel':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Temos um empate!''')
            print()
            empate += 1
        elif opcao == 'tesoura' and opcaoPC == 'tesoura':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Temos um empate!''')
            print()
            empate += 1
        elif opcao == 'tesoura' and opcaoPC == 'papel':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Tesoura corta Papel. Você ganhou!''')
            print()
            usuario += 1
        elif opcao == 'pedra' and opcaoPC == 'papel':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Papel embrulha a Pedra. Você perdeu!''')
            print()
            pc += 1
        elif opcao == 'pedra' and opcaoPC == 'tesoura':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Pedra amassa a Tesoura. Você ganhou!''')
            print()
            usuario += 1
        elif opcao == 'papel' and opcaoPC == 'tesoura':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Tesoura corta Papel. Você perdeu!''')
            print()
            pc += 1
        elif opcao == 'papel' and opcaoPC == 'pedra':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Papel embrulha a Pedra. Você ganhou!''')
            print()
            usuario += 1
        elif opcao == 'tesoura' and opcaoPC == 'pedra':
            print(f'''
            Eu tirei: {opcaoPC}!
            Você tirou: {opcao}!
            Tesoura corta Papel. Você ganhou!''')
            print()
            usuario += 1
            #Fim do bloco do jogo
#Esse bloco pergunta ao usuário se vai jogar novamente.
    #Se for jogar novamente, roda o While novamente.
    continuar = str(input('Deseja jogar novamente? S/N ')).strip().upper()
    if continuar[0] == 'S':
        quer_continuar = True
    else: 
        break
    #Fim do Bloco que decide a repetição do While
#Inicio do bloco de pontuação total jogo
#Calculando placar
if empate > usuario and empate > pc:
    print(f'''
    O jogo foi acirrado mas nós empatamos!

    Placar:
    Total de jogos: {cont_rodadas}.
    Empates: {empate}
    Suas vitórias: {usuario}
    Minhas vitórias: {pc}''')
elif usuario > pc and usuario > empate:
    print(f'''
    O jogo foi acirrado mas você venceu!

    Placar:
    Total de jogos: {cont_rodadas}.
    Empates: {empate}
    Suas vitórias: {usuario}
    Minhas vitórias: {pc}''')
elif pc > usuario and pc > empate:
    print(f'''
    O jogo foi acirrado mas eu venci!

    Placar:
    Total de jogos: {cont_rodadas}.
    Empates: {empate}
    Suas vitórias: {usuario}
    Minhas vitórias: {pc}''')
    #Fim do bloco de pontuação total jogo