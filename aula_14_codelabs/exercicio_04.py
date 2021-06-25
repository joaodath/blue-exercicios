#Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário 
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha 
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas
#Definindo Funções
def calc_salario(horas_semanais, valor_da_hora):
    if horas_semanais > 40:
        sal = (valor_da_hora * horas_semanais) + (horas_semanais * 1.5)
        return sal
    else:
        sal = valor_da_hora * horas_semanais
        return sal
def limpa_tela():
    import os
    import sys
    #Limpando a tela do Interpretador no Windows
    if sys.platform.startswith('win32') or sys.platform.startswith('cigwin'):
        clear = lambda: os.system('cls')
        return clear()
    else:
        #Limpando a tela do Interpretador no Linux
        clear = lambda: os.system('clear')
        return clear()
    #Okay, agora podemos continuar :)
#Programa Principal
#Este programa pode ser integrado com o código de cadastro_de_funcionario.py numa próxima versão
limpa_tela()
lista_de_funcionarios = list()
quer_continuar = True
#Vamos tornar nosso código atemporal pegando a data do sistema
import datetime
now = datetime.datetime.now()
ano_atual = now.year
mes_atual = ''
if now.month == 1:
    mes_atual = 'Janeiro'
elif now.month == 2:
    mes_atual = 'Fevereiro'
elif now.month == 3:
    mes_atual = 'Março'
elif now.month == 4:
    mes_atual = 'Abril'
elif now.month == 5:
    mes_atual = 'Maio'
elif now.month == 6:
    mes_atual = 'Junho'
elif now.month == 7:
    mes_atual = 'Julho'
elif now.month == 8:
    mes_atual = 'Agosto'
elif now.month == 9:
    mes_atual = 'Setembro'
elif now.month == 10:
    mes_atual = 'Outubro'
elif now.month == 11:
    mes_atual = 'Novembro'
elif now.month == 12:
    mes_atual = 'Dezembro'
#Agora a gente informa ao usuário qual foi o ano que o sistema informou
print(f'''
Iniciando Programa de Salário de Funcionários.

Seu computador informou o ano atual como {ano_atual} e o mês atual como {mes_atual}.
''')
#Agora a gente questiona se o usuário quer alterar o ano usado para os cálculos
quer_mudar_ano = str(input('Você quer mudar o ano usado para os cálculos? S/N ')).strip().upper()[0]
print()
if quer_mudar_ano == 'S':
    ano_atual = int(input('Informe o ano atual (apenas números): '))
    print(f'Você informou: {ano_atual}')
elif quer_mudar_ano == 'N':
    print('Okay! Vamos continuar!')
else:
    quer_continuar = False
    print('''
    Ops. Você não informou um valor válido.
    O programa foi encerrado.
    ''')
#Agora a gente questiona se o usuário quer alterar o mês usado para os cálculos
quer_mudar_mes = str(input('Você quer mudar o mês usado para os cálculos? S/N ')).strip().upper()[0]
print()
if quer_mudar_mes == 'S':
    mes_atual = int(input('Informe o mês atual (apenas números): '))
    print(f'Você informou: {mes_atual}')
elif quer_mudar_mes == 'N':
    print('Okay! Vamos continuar!')
else:
    quer_continuar = False
    print('''
    Ops. Você não informou um valor válido.
    O programa foi encerrado.
    ''')
#Fim do Bloco de Ano Atual
while quer_continuar == True:
    quer_continuar = False
    funcionario = dict()
    nome = str(input('Informe o nome do funcionário: ')).strip().capitalize()
    funcionario['nome'] = nome
    funcionario['mes'] = mes_atual
    print(f'Okay, vamos começar a calcular o salário de {nome} para {mes_atual}!')
    print()
    semanas = int(input(f'Quantas semanas {nome} trabalhou em {mes_atual}? '))
    funcionario['semanas_trabalhadas'] = semanas
    valor_hora = input(f'Informe o valor da hora trabalhada para {nome}: ').strip().replace('R$', '').replace('r$', '').replace('$', '')
    valor_hora = int(valor_hora)
    funcionario['valor_da_hora'] = valor_hora
    salario = 0
    for i in range(semanas):
        horas = input(f'Informe a quantidade de horas trabalhadas na semana {i+1} por {nome}: ').strip().replace('horas', '').replace('HORAS', '')
        horas = int(horas)
        salario += calc_salario(horas, valor_hora)
    funcionario['salario'] = salario
    print()
    print(f'O salário de {nome} é R${salario}.')
    print()
    lista_de_funcionarios.append(funcionario.copy())
    quer_continuar_input = str(input('Deseja cadastrar um novo funcionário? S/N ')).strip().upper()
    if quer_continuar_input[0] == 'S':
        quer_continuar = True
    else:
        break
print()
quer_ver = str(input('Quer ver a lista com os funcionários cadastrados? S/N ')).strip().upper()
#Suponho que o bloco abaixo pode ser melhorado com o uso de Pandas e Nested Dictionary
if quer_ver[0] == 'S':
    print()
    for k in lista_de_funcionarios:
        lista2 = list(k.items())
        print(f'Lista de Salários de Funcionários: {lista2}')
    print()
    print('Okay! Programa finalizado!')
else:
    print()
    print('Okay! Programa finalizado!')





