# Exercício Treino 01 - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes 
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}
# Exercício Treino 02 - Crie um dicionário em que suas chaves correspondem a números 
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
#refazer dicionário com zip do dict
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
#Exclusivamente o exercício proposto
print('''
Este programa é o Exercício 01 e 02 da Aula 12
Módulo 01: Lógica de Programação em Python''')
print('''
Apresentando os valores do exercício proposto 01''')
# dicio_proposto = {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81} #Informando diretamente
# print(dicio_proposto)
#OR
print()
dicio_proposto1 = {1: 0, 4: 0, 5: 0, 6: 0, 7: 0, 9: 0}
for k in dicio_proposto1.keys():
    dicio_proposto1[k] = k ** 2
print(dicio_proposto1)
print()
sleep(3)
print('''
Apresentando os valores do exercício proposto 02''')
print()
dicio_proposto2 = dict()
for c in range(1,11):
    dicio_proposto2[c] = c ** 2
print(dicio_proposto2)
print()
#Loop for para avisar que a tela será limpa
for i in range(10, 0, -1):
    print(f'A tela será limpa em {i} segundos')
    sleep(1)
#Fim do Exercício Proposto
#Limpando a tela
if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
    #Limpando a tela do Interpretador no Windows
    clear = lambda: os.system('cls')
    clear()
else:
    #Limpando a tela do Interpretador no Linux
    clear = lambda: os.system('clear')
    clear()
#Bônus do João: coletandos valores via input enquanto o usuário continuar informando-os
dicio_do_exercicio = dict()
quer_continuar = True
print('''
Olá! Este programa cria um dicionário com chaves de
números inteiros e preenche os valores
com o quadrado (expoente 2) da chave''')
print()
while quer_continuar == True:
    print()
    dicio_key = int(input('Informe a chave para o dicionário (valor inteiro): '))
    dicio_do_exercicio[dicio_key] = dicio_key ** 2
    print()
    quer_continuar_pergunta = str(input('Deseja adicionar um novo valor? S/N ')).strip().upper()
    if quer_continuar_pergunta[0] == 'S':
        quer_continuar = True
    else:
        quer_continuar = False
        print(f'''
        Okay! Você quem manda!
        Programa encerrado!
        Estes foram os valores salvos no dicionário:
        {dicio_do_exercicio}''')