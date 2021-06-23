# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma 
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas. x
# B) A média da idade. x 
# C) Uma lista com as mulheres. x 
# D) Uma lista com as idades que estão acima da média. X
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando x
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não. x
from time import sleep
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
#Inicializando as listas necessárias
lista_de_pessoas = list()
lista_mulheres = list()
lista_mulheres_idade_acima = list()
#Inicializando variável de controle do Bloco While
quer_continuar = True
valida_sexo = False
#Inicializando variáveis necessárias
quant_pessoas = todas_idades = media_idades = cont_voltas = 0
#Bloco While recebendo dados das pessoas via input do usuário
while quer_continuar == True:
    cont_voltas += 1
    dicionario_temp = dict()
    nome = str(input('Informe o nome da pessoa: ')).strip().capitalize()
    sexo_biologico = str(input(f'Informe o sexo biológico de {nome}: ')).strip().lower()
    #Bloco If inicia a validação de sexo biológico
    if sexo_biologico[0] in 'f' or sexo_biologico[0] in 'm':
        valida_sexo = False #Não precisa pedir para inserir novamente
    elif sexo_biologico[0] not in 'f' or sexo_biologico[0] not in 'm':
        valida_sexo = True #Precisa pedir para inserir novamente
        #Bloco While fazendo a validação de sexo biológico
        while valida_sexo == True:
            print('Sexo biológico informado inválido. Por favor informe novamente')
            sexo_biologico = str(input(f'Informe o sexo biológico de {nome}: ')).strip().lower()
            #Bloco If inicia a validação de sexo biológico
            if sexo_biologico[0] in 'f' or sexo_biologico[0] in 'm':
                valida_sexo = False #O Bloco While de validação de sexo biológico é finalizado.
            else:
                valida_sexo = True #O Bloco While de validação de sexo biológico roda novamente.
    idade = int(input(f'Informe a idade de {nome} (apenas números): '))
    #somas as idades
    todas_idades += idade
    #guarda os dados no dicionário temporário
    dicionario_temp['nome'] = nome
    dicionario_temp['sexo_biologico'] = sexo_biologico
    dicionario_temp['idade'] = idade
    #Bloco If para decidir se coloca na lista de mulheres ou não
    if sexo_biologico[0] == 'f':
        lista_mulheres.append(dicionario_temp.copy())
        print(f'Adicionei na lista lista_mulheres: {lista_mulheres}')
    #copia os dados para uma lista composta de dicionários. ver depois dicionário aninhado.
    lista_de_pessoas.append(dicionario_temp.copy())
    #verifica se o usuário quer informar uma nova pessoa para o dicionário
    continuar = str(input('''
    Quer informar os dados de outra pessoa? 
    Digite "Sim" para continuar ou qualquer tecla + enter para sair. ''')).strip().upper()
    if continuar[0] == 'S':
        quer_continuar = True #Se o usuário responde "Sim", a variável de controle é True e o While continua rodando.
    else:
        quer_continuar = False #Se o usuário responde "Não", a variável de controle é False e o While para de rodar.
        print()
        print('Okay! Não vamos mais cadastrar outras pessoas.')
#Média de Idades
media_idades = todas_idades / cont_voltas
media_idades = int(media_idades) #Uso o int para limpar o decimal sem arredondar o valor
#Um bloco só pra melhorar a UX
print('Por favor, aguarde. Estou preparando os dados.')
for c in range(3):
    print('Aguarde...')
    sleep(1)
print()
#Processando lista_mulheres e adicionando em lista_mulheres_idade_acima todas as mulheres acima da idade média
for index, v in enumerate(lista_mulheres):
    if lista_mulheres[index].get('idade') > media_idades:
        lista_mulheres_idade_acima.append(lista_mulheres[index].copy())
print(f'''
Okay. Estou pronto!
Exibindo dados agora:

O número de pessoas cadastradas foi {len(lista_de_pessoas)}.

A média de idades foi {media_idades}.
''')
#Esse bloco If verifica se há mulheres cadastradas
if len(lista_mulheres) > 0:
    print(f'O número de mulheres cadastradas foi {len(lista_mulheres)}.') #Se houver mulheres, ele imprime a quantidade total de mulheres.
    print()
    if len(lista_mulheres_idade_acima) > 1: #Esse If verifica se há mais que uma mulher acima da idade média para imprimir o texto com os substantivos e verbos concordando em número.
        print(f'{lista_mulheres_idade_acima} estão acima da média de idade geral que é {media_idades} anos.')
        print()
    elif len(lista_mulheres_idade_acima) == 1: #Esse Elif verifica se há apenas uma mulher acima da idade média para imprimir o texto com os substantivos e verbos concordando em número.
        print(f'Apenas 1 mulher está acima da idade média geral que é {media_idades}.')
        print()
    else: #Esse Else roda se não houver mulheres acima da idade média cadastradas para informar isso ao usuário
        print('Não há mulheres acima da idade média.')
    print('As mulheres cadastradas são:') #Esse print roda apenas se houver mulheres cadastradas
    for index, v in enumerate(lista_mulheres): #Esse For acessa a lista lista_mulheres e mprime nome e idade das mulheres cadastradas. Usa-se o enumerate para obter o índice da lista
        nome = lista_mulheres[index].get('nome') #Acessa a chave 'nome' no dicionário que está na posição 'index' da lista lista_mulheres
        idade = lista_mulheres[index].get('idade') #Acessa a chave 'idade' no dicionário que está na posição 'index' da lista lista_mulheres
        print(f'{nome}, {idade} anos.') #Finalmente imprime os dados da lista lista_mulheres
else: #Roda se não houver mulheres cadastradas informando o usuário sobre isso
    print('Não há mulheres cadastradas.')
