# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

#Cadastro de Funcionários alpha por João Rodrigues
#Vamos limpar as coisas por aqui?
import os
#Limpando a tela do Interpretador no Windows
clear = lambda: os.system('cls')
clear()
#Limpando a tela do Interpretador no Linux
clear = lambda: os.system('clear')
clear()
#Okay, agora podemos continuar :)
#Vamos tornar nosso código atemporal pegando a data do sistema
import datetime
now = datetime.datetime.now()
ano_atual = now.year
#Agora a gente informa ao usuário qual foi o ano que o sistema informou
print(f'''
Iniciando Programa de Cadastro de Funcionários.

Seu computador informou o ano atual como {ano_atual}.
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
    print('''
    Ops. Você não informou um valor válido.
    O programa foi encerrado.
    ''')
#Fim do Bloco de Ano Atual
#Declaração de variáveis que vamos usar
nome = ''
ano_de_nascimento = ctps = ano_de_contratacao = salario = idade = aposentadoria = 0
funcionario = dict()
lista_de_funcionarios = list()
quer_continuar = True
while quer_continuar == True:
    nome = str(input('Informe o nome do funcionário: ')).strip().capitalize()
    funcionario['nome'] = nome
    print(f'Okay, vamos começar o cadastro de {nome}!')
    print()
    ano_de_nascimento = int(input(f'Informe o ano de nascimento de {nome} (apenas números): '))
    funcionario['nascimento'] = ano_de_nascimento
    idade = ano_atual - ano_de_nascimento
    funcionario['idade'] = idade
    ctps = int(input('Informe o número da CTPS do funcionário ou digite 0 se não for funcionário: '))
    funcionario['ctps'] = ctps
    if ctps != 0:
        ano_de_contratacao = int(input(f'Informe o ano de contratação de {nome} (apenas números): '))
        funcionario['ano_de_contratacao'] = ano_de_contratacao
        salario = float(input(f'Informe o salário atual de {nome}. Apenas números, ex: 4200.00 '))
        funcionario['salario'] = salario
    aposentadoria = (ano_atual - ano_de_contratacao) - 35
    if aposentadoria < 0 and ctps != 0:
        aposentadoria = aposentadoria * -1
        print(f'{nome} estará apto(a) para se aposentar após {aposentadoria} anos de trabalho.')
        funcionario['aposentadoria'] = aposentadoria
    elif aposentadoria > 0 and ctps != 0:
       print(f'''
       {nome} está apto(a) para se aposentar há {aposentadoria} anos.
       Ou seja, {nome} poderia estar aposentado  {ano_atual - aposentadoria}!''')
       funcionario['aposentadoria'] = aposentadoria
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
        print(f'Lista de Funcionários: {lista2}')
    print()
    print('Okay! Programa finalizado!')
else:
    print()
    print('Okay! Programa finalizado!')
    

