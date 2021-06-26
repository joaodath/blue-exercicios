#Programa do Projeto Detetive, melhorado com códigos extras. - João Rodrigues
#Importando biblioteca OS e SYS para limpar a tela
import os
import sys
if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
    #Limpando a tela do Interpretador no Windows
    clear = lambda: os.system('cls')
    clear()
else:
    #Limpando a tela do Interpretador no Linux
    clear = lambda: os.system('clear')
    clear()
#Okay, agora podemos continuar :)
#Obtendo dados de data do sistema
import datetime
now = datetime.datetime.now()
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
#Início do Programa
soma = 0 #Inicializando variável de nível de suspeita
#Abertura Bonitinha
print()
print('-*' * 20)
print()
print(f'''
Bem vindo(a) ao Sistema de Interrogatório Inteligente da Polícia Federal.
SIIPF v.1.0

Hoje é {now.day} de {mes_do_ano} de {now.year} e são {now.hour}h{now.minute}m.
Seu interrogatório será salvo no arquivo {now.year}{now.month}{now.day}{now.hour}{now.minute}{now.microsecond}.siipf1

Responda as perguntas a seguir para agilizarmos o tratamento do seu caso.
Ao responder, você concorda que os dados serão processados, armazenados e compartilhados entre os escritórios da Polícia Federal e dos Governos Municipal, Estadual e Federal, conforme o que está disposto na LGPD.

ATENÇÃO: SALA TRANCADA AUTOMATICAMENTE.
''')
print()
print('-*' * 20)
print()
#Começo do Interrogatório
tel = str(input('Você telefonou para a vítima? S/N ')) #Recebe Resposta 01
#Checando resposta 01
if tel.strip().upper().startswith('S'):
  soma += 1
  print('Resposta: Sim')
elif tel.strip().upper().startswith('N'):
  print('Resposta: Não')
else:
  print('Resposta Inválida. Fechando o programa.')
  exit()
local = str(input('Você esteve no local do crime? S/N ')) #Recebe Resposta 02
#Checando resposta 02
if local.strip().upper().startswith('S'):
  soma += 1
  print('Resposta: Sim')
elif local.strip().upper().startswith('N'):
  print('Resposta: Não')
else:
  print('Resposta Inválida')
  exit()
#Checando resposta 03
end = str(input('Você mora perto da vítima? S/N ')) #Recebe Resposta 03
if end.strip().upper().startswith('S'):
  soma += 1
  print('Resposta: Sim')
elif end.strip().upper().startswith('N'):
  print('Resposta: Não')
else:
  print('Resposta Inválida')
  exit()
din = str(input('Você devia para a vítima? S/N ')) #Recebe Resposta 04
#Checando resposta 04
if din.strip().upper().startswith('S'):
  soma += 1
  print('Resposta: Sim')
elif din.strip().upper().startswith('N'):
  print('Resposta: Não')
else:
  print('Resposta Inválida')
  exit()
trab = str(input('Você já trabalhou com a vítima? S/N ')) #Recebe Resposta 05
#Checando resposta 05
if trab.strip().upper().startswith('S'):
  soma += 1
  print('Resposta: Sim')
elif trab.strip().upper().startswith('N'):
  print('Resposta: Não')
else:
  print('Resposta Inválida')
  exit()
if soma == 0:
  print('Você foi considerado(a) inocente! Pode ir para casa.')
elif 0 < soma <= 2:
  print('''
  ATENÇÃO: SALA TRANCADA AUTOMATICAMENTE.
  Você foi considerado(a) suspeito(a)! 
  Permaneça na delegacia!
  Um agente já foi alertado e irá conversar com você.''')
elif 2 < soma <= 4:
  print('Você foi considerado(a) cúmplice!')
elif soma == 5:
  print('''
  ATENÇÃO: SALA TRANCADA AUTOMATICAMENTE.
  Você foi considerado(a) assassino(a)! 
  Permaneça na delegacia!
  Um agente já foi alertado e irá conversar com você.''')
#Fim do Programa