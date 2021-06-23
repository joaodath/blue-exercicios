#Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para 
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é 
# reprovado.
#Adicionando bônus: o programa também lê as três notas do aluno
#Importando biblioteca datetime para verificar e depois imprimir data
import datetime
now = datetime.datetime.now()
# print(now.year, now.month, now.day, now.hour, now.minute, now.second)
mes_do_ano = ''
if now.month == 1:
    mes_do_ano = 'Janeiro'
elif now.month == 2:
    mes_do_ano = 'Fevereiro'
elif now.month == 3:
    mes_do_ano = 'Março'
elif now.month == 4:
    mes_do_ano = 'Abril'
elif now.month == 5:
    mes_do_ano = 'Maio'
elif now.month == 6:
    mes_do_ano = 'Junho'
elif now.month == 7:
    mes_do_ano = 'Julho'
elif now.month == 8:
    mes_do_ano = 'Agosto'
elif now.month == 9:
    mes_do_ano = 'Setembro'
elif now.month == 10:
    mes_do_ano = 'Outubro'
elif now.month == 11:
    mes_do_ano = 'Novembro'
elif now.month == 12:
    mes_do_ano = 'Dezembro'
#Fim da Importação de datetime
#Importando biblioteca OS e SYS para limpar a tela
import os
import sys
from time import sleep
if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
    #Limpando a tela do Interpretador no Windows
    clear = lambda: os.system('cls')
    clear()
else:
    #Limpando a tela do Interpretador no Linux
    clear = lambda: os.system('clear')
    clear()
#Okay, agora podemos continuar :)
print(f'''
Bem vinde ao Programa de Boletins da Escola Mochileiros da Galáxia
Esta é a versão Alpha do programa.

Hoje é {now.day} de {mes_do_ano} de {now.year}.

Vamos começar a verificar a situação dos Alunos?

O cálculo é de Média Simples (não considera peso).
Tenha em mãos as notas de AV1, AV2 e AV3 de cada trimestre.
Ao final, irei calcular a média parcial (de cada trimestre)
e a média final (do ano).

''')
quer_continuar = True
# dicio_final = dict() #Aqui é para tentar um dicionário aninhado e/ou pandas na versão beta
lista_de_alunos = list() #Recebe os dados temporários para criar uma lista de dicionários
#Bloco que recebe os dados dos alunos
while quer_continuar == True:
    dicio_temp = dict() #Pegando dados informados temporariamente
    nome = str(input('Informe o nome do aluno para começar: ')).strip().capitalize()
    dicio_temp['nome_do_aluno'] = nome
    nota_av1_tri1 = float(input(f'Informe a nota da AV1 do 1º trimestre de {nome}: '))
    dicio_temp['nota_av1_tri1'] = nota_av1_tri1
    nota_av2_tri1 = float(input(f'Informe a nota da AV2 do 1º trimestre de {nome}: '))
    dicio_temp['nota_av2_tri1'] = nota_av2_tri1
    nota_av3_tri1 = float(input(f'Informe a nota da AV3 do 1º trimestre de {nome}: '))
    dicio_temp['nota_av3_tri1'] = nota_av3_tri1
    nota_av1_tri2 = float(input(f'Informe a nota da AV1 do 2º trimestre de {nome}: '))
    dicio_temp['nota_av1_tri2'] = nota_av1_tri2
    nota_av2_tri2 = float(input(f'Informe a nota da AV2 do 2º trimestre de {nome}: '))
    dicio_temp['nota_av2_tri2'] = nota_av2_tri2
    nota_av3_tri2 = float(input(f'Informe a nota da AV3 do 2º trimestre de {nome}: '))
    dicio_temp['nota_av3_tri2'] = nota_av3_tri2
    nota_av1_tri3 = float(input(f'Informe a nota da AV1 do 3º trimestre de {nome}: '))
    dicio_temp['nota_av1_tri3'] = nota_av1_tri3
    nota_av2_tri3 = float(input(f'Informe a nota da AV2 do 3º trimestre de {nome}: '))
    dicio_temp['nota_av2_tri3'] = nota_av2_tri3
    nota_av3_tri3 = float(input(f'Informe a nota da AV3 do 3º trimestre de {nome}: '))
    dicio_temp['nota_av3_tri3'] = nota_av3_tri3
    #Bloco calculando as médias
    mediatri1 = (nota_av1_tri1 + nota_av2_tri1 + nota_av3_tri1) / 3
    mediatri2 = (nota_av1_tri2 + nota_av2_tri2 + nota_av3_tri2) / 3
    mediatri3 = (nota_av1_tri3 + nota_av2_tri3 + nota_av3_tri3) / 3
    mediafinal = (mediatri1 + mediatri2 + mediatri3) / 3
    dicio_temp['mediatri1'] = mediatri1
    dicio_temp['mediatri2'] = mediatri2
    dicio_temp['mediatri3'] = mediatri3
    dicio_temp['mediafinal'] = mediafinal
    #Bloco calculando situação
    if mediafinal >= 7:
        situacao = 'APROVADO'
        dicio_temp['situacao'] = situacao
    elif 5 >= mediafinal < 7:
        situacao = 'RECUPERAÇÃO'
        dicio_temp['situacao'] = situacao
    elif mediafinal < 5:
        situacao = 'REPROVADO'
        dicio_temp['situacao'] = situacao
    lista_de_alunos.append(dicio_temp.copy()) #Envia os dados para uma lista composta
    print(f'''
    A média final de {nome} é {mediafinal:.2f}.
    SITUAÇÃO: {situacao}
    
    Informação Salva!''')
    #Verifica se o usuário deseja informar dados de outro aluno
    continuar = str(input('''
    Quer informar os dados de um outro aluno? 
    Digite "Sim" para continuar ou digite qualquer tecla para sair. ''')).strip().upper()
    if continuar[0] == 'S':
        quer_continuar = True #Se o usuário quiser inserir mais dados, a variável de controle se mantém True
    else:
        quer_continuar = False #Se o usuário não quiser inserir mais dados, a variável de controle muda para False
        print()
#Bloco verificando se o usuário quer imprimir os dados informados na tela
visualizar_dados = str(input('''
Você quer ver os dados salvos?
Digite "Sim" para continuar ou digite qualquer tecla para sair. ''')).strip().upper()
if visualizar_dados[0] == 'S':
    for index, a in enumerate(lista_de_alunos): #Loop na lista composta imprimindo todos os itens, linha por linha
        print(f'{index}: {a}')
        print()
    print()
    print('Programa encerrado!') #Depois de imprimir, o programa é encerrado
else:
    print('Programa encerrado!') #O programa é encerrado por não ter mais códigos
#Fim do Programa