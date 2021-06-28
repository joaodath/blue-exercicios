# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer; X
# • Guardar os resultados dos dados em um dicionário. X 
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número 
# no dado. --> final (ordenar as chaves, quem ganhou vem primeiro) X
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande 
# campeão. 
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 16
#Inicio
#Importa bibliotecas necessárias
from random import randint
from time import sleep
#Código para Limpar a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')
#Programa Principal
#Apresentação do Programa
print()
print('-*' * 20)
print()
print('''
Bem vindo(a) ao Jogo de Dados Aleatórios!.

Neste jogo, quatro jogadores irão rolar um dado. 
Quem tirar o maior número no dado, vence a partida!
O Grande Campeão é aquele que ganhar em mais partidas.

Atenção: o Grande Campeão só será exibido se você decidir não jogar mais.
Se você quiser jogar novas partidas, eu irei esperar todas as partidas 
terminarem para mostrar o Grande Campeão.

O JOGO VAI COMEÇAR!
''')
print()
print('-*' * 20)
print()
sleep(2)
#Declarando variáveis que vão guardar o número de vitórias, empates e rodadas
jogador1 = jogador2 = jogador3 = jogador4 = empate = cont_rodadas = 0
pont_primeiro_lugar = pont_segundo_lugar = pont_terceiro_lugar = pont_quarto_lugar = 0
primeiro_lugar = segundo_lugar = terceiro_lugar = quarto_lugar = ''
nome_jogador1 = 'Jogador 1'
nome_jogador2 = 'Jogador 2'
nome_jogador3 = 'Jogador 3'
nome_jogador4 = 'Jogador 4'
#Obtendo nome dos jogadores
print(f'''
Os nomes dos jogadores são:
{nome_jogador1}
{nome_jogador2}
{nome_jogador3}
{nome_jogador4}
''')
sleep(2)
mudar_nome = str(input('Quer mudar os nomes dos jogadores? S/N ').strip().upper())
if mudar_nome.startswith('S'):
    nome_jogador1 = str(input('Informe o nome do Jogador 1: ').strip().capitalize())
    nome_jogador2 = str(input('Informe o nome do Jogador 2: ').strip().capitalize())
    nome_jogador3 = str(input('Informe o nome do Jogador 3: ').strip().capitalize())
    nome_jogador4 = str(input('Informe o nome do Jogador 4: ').strip().capitalize())
    sleep(1)
else:
    print('Okay! Vou usar o nome padrão de cada jogador!')
    sleep(1)
    print()
#Declarando dicionário
partidas = {nome_jogador1: 0,
            nome_jogador2: 0,
            nome_jogador3: 0,
            nome_jogador4: 0
            }
partidas_total = {nome_jogador1: list(),
                    nome_jogador2: list(),
                    nome_jogador3: list(),
                    nome_jogador4: list()}
partidas_total_ordenado = dict()
#Abrindo Variável de Controle
quer_continuar = True
#Rolando os dados
while quer_continuar == True:
    #Obtendo número de rodadas
    rodadas = int(input('Quantas partidas serão feitas? '))
    for i in range(rodadas):
        cont_rodadas += 1 #Contador de partidas totais. Se o usuário roda 2x dps roda + 4x, o total é 6 partidas.       
        for k in partidas.keys():
            dado = randint(1,6)
            partidas[k] = dado
            partidas_total[k].append(dado)
        if partidas[nome_jogador1] > partidas[nome_jogador2] and partidas[nome_jogador1] > partidas[nome_jogador3] and partidas[nome_jogador1] > partidas[nome_jogador4]:
            jogador1 += 1
            sleep(1)
            print()
            print(f'O {nome_jogador1} ganhou a Partida {i+1}!')
        elif partidas[nome_jogador2] > partidas[nome_jogador1] and partidas[nome_jogador2] > partidas[nome_jogador3] and partidas[nome_jogador2] > partidas[nome_jogador4]:
            jogador2 += 1
            sleep(1)
            print()
            print(f'O {nome_jogador2} ganhou a Partida {i+1}!')
        elif partidas[nome_jogador3] > partidas[nome_jogador2] and partidas[nome_jogador3] > partidas[nome_jogador1] and partidas[nome_jogador3] > partidas[nome_jogador4]:
            jogador3 += 1
            print()
            print(f'O {nome_jogador3} ganhou a Partida {i+1}!')
        elif partidas[nome_jogador1] > partidas[nome_jogador2] and partidas[nome_jogador1] > partidas[nome_jogador3] and partidas[nome_jogador1] > partidas[nome_jogador4]:
            jogador4 += 1
            sleep(1)
            print()
            print(f'O {nome_jogador4} ganhou a Partida {i+1}!')
        else:
            empate += 1
            sleep(1)
            print()
            print(f'Houve empate na Partida {i+1}!')
        sleep(2)
        #Imprimir o dicionário da partida
        print(f'''
        Os dados tirados na Partida {i+1} foram: 
        {partidas}.
        Houve {empate} empate(s) até agora!''')
        sleep(1)
        print()
    quer_continuar_pergunta = str(input('Deseja jogar novamente? S/N ').strip().upper())
    print()
    if quer_continuar_pergunta.startswith('S'):
        quer_continuar = True
    else:
        quer_continuar = False
#Esse bloco descobre a ordem dos vencedores e grava a pontuação total de cada um
#A lista armazena e depois organiza os jogadores do maior para o menor de acordo com o número de vitórias
lista_temporaria = [jogador1, jogador2, jogador3, jogador4]
lista_temporaria = sorted(lista_temporaria, reverse= -1)
#jogador1
if lista_temporaria[0] == jogador1 and primeiro_lugar == '':
    primeiro_lugar = nome_jogador1
    pont_primeiro_lugar = jogador1
elif lista_temporaria[1] == jogador1 and segundo_lugar == '':
    segundo_lugar = nome_jogador1
    pont_segundo_lugar = jogador1
elif lista_temporaria[2] == jogador1 and terceiro_lugar == '':
    terceiro_lugar = nome_jogador1
    pont_terceiro_lugar = jogador1
elif lista_temporaria[3] == jogador1 and quarto_lugar == '':
    quarto_lugar = nome_jogador1
    pont_quarto_lugar = jogador1
#jogador2
if lista_temporaria[0] == jogador2 and primeiro_lugar == '':
    primeiro_lugar = nome_jogador2
    pont_primeiro_lugar = jogador2
elif lista_temporaria[1] == jogador2 and segundo_lugar == '':
    segundo_lugar = nome_jogador2
    pont_segundo_lugar = jogador2
elif lista_temporaria[2] == jogador2 and terceiro_lugar == '':
    terceiro_lugar = nome_jogador2
    pont_terceiro_lugar = jogador2
elif lista_temporaria[3] == jogador2 and quarto_lugar == '':
    quarto_lugar = nome_jogador2
    pont_quarto_lugar = jogador2
#jogador3
if lista_temporaria[0] == jogador3 and primeiro_lugar == '':
    primeiro_lugar = nome_jogador3
    pont_primeiro_lugar = jogador3
elif lista_temporaria[1] == jogador3 and segundo_lugar == '':
    segundo_lugar = nome_jogador3
    pont_segundo_lugar = jogador3
elif lista_temporaria[2] == jogador3 and terceiro_lugar == '':
    terceiro_lugar = nome_jogador3
    pont_terceiro_lugar = jogador3
elif lista_temporaria[3] == jogador3 and quarto_lugar == '':
    quarto_lugar = nome_jogador3
    pont_quarto_lugar = jogador3
#jogador4
if lista_temporaria[0] == jogador4 and primeiro_lugar == '':
    primeiro_lugar = nome_jogador4
    pont_primeiro_lugar = jogador4
elif lista_temporaria[1] == jogador4 and segundo_lugar == '':
    segundo_lugar = nome_jogador4
    pont_segundo_lugar = jogador4
elif lista_temporaria[2] == jogador4 and terceiro_lugar == '':
    terceiro_lugar = nome_jogador4
    pont_terceiro_lugar = jogador4
elif lista_temporaria[3] == jogador4 and quarto_lugar == '':
    quarto_lugar = nome_jogador4
    pont_quarto_lugar = jogador4
#Criando um novo dicionário ordenado do Primeiro ao Quarto Lugar
partidas_total_ordenado[primeiro_lugar] = partidas_total[primeiro_lugar].copy()
partidas_total_ordenado[segundo_lugar] = partidas_total[segundo_lugar].copy()
partidas_total_ordenado[terceiro_lugar] = partidas_total[terceiro_lugar].copy()
partidas_total_ordenado[quarto_lugar] = partidas_total[quarto_lugar].copy()
partidas_total = partidas_total_ordenado #Dicionário original recebe o novo dicionário ordenado
print(f'''
Ufa! O jogo foi acirradíssimo, mas tudo tem um fim.
Foram feitas {cont_rodadas} rodada(s).''')
sleep(2)
if jogador1 > 0 or jogador2 > 0 or jogador3 > 0 or jogador4 > 0:
    print('E o grande campeão de hoje é', end='')
    sleep(1)
    print('.', end=' ')
    sleep(1)
    print('.', end=' ')
    sleep(1)
    print('.', end= ' ')
    sleep(1)
    print(f' {primeiro_lugar}!')
    sleep(3)
    print(f'''
    __* Lista de Vencedores *__
    1º lugar: {primeiro_lugar} com {pont_primeiro_lugar} vitórias!
    2º lugar: {segundo_lugar} com {pont_segundo_lugar} vitórias!
    3º lugar: {terceiro_lugar} com {pont_terceiro_lugar} vitórias!
    4º lugar: {quarto_lugar} com {pont_quarto_lugar} vitórias!
    Empates: {empate} empate(s)!
    ''')
else:
    print(f'Não houve ganhadores! Houve {empate} empate(s)!')
sleep(1)
#Print do Dicionário Ordenado desativado, ative removendo o próximo '#'
#print(f'\nDicionário Ordenado do Primeiro ao Quarto Lugar: \n{partidas_total}')
print('Fim do Jogo!')