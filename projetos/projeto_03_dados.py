# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 
# jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer; X
# • Guardar os resultados dos dados em um dicionário. 
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número 
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande 
# campeão.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 16
from random import randint
quer_continuar_1 = True
quer_continuar_2 = True
quer_continuar_3 = True
quer_continuar_4 = True
while quer_continuar_1 == True:
    rodadas = int(input('Quantas rodadas iremos jogar? '))
    #Bloco para Fazer a Escolha do Computador
    for i in range(4):
        for c in range(rodadas):
            roll_the_dice = randint(1,6)

