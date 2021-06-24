# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:
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
#declarando função
def voto():
    #Vamos tornar nosso código atemporal pegando a data do sistema
    import datetime
    now = datetime.datetime.now()
    ano_atual = now.year
    #Okay, agora eu sei o ano informado pelo sistema
    ano_nasc = int(input('Informe o ano de nascimento: '))
    idade = ano_atual - ano_nasc
    if 18 <= idade < 70:
        return f'Idade: {idade} - Voto Obrigatório'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Idade: {idade} - Voto Opcional'
    else:
        return f'Idade: {idade} - Voto Negado'
    # elif idade < 16:
    #     return f'Idade: {idade}: Voto Negado'
#código
situacao_voto = voto()
print(situacao_voto)