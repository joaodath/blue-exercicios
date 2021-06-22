# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

#Cadastro de Funcionários alpha por João Rodrigues
import datetime
from typing import Dict #Vamos tornar nosso código atemporal pegando a data do sistema
now = datetime.datetime.now()
ano_atual = now.year
#Agora a gente informa ao usuário qual foi o ano que o sistema informou
print(f'''
Seu computador informou o ano atual como {ano_atual}.
Iniciando Programa de Cadastro de Funcionários
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
funcionario = Dict()

quer_continuar == True
while quer_continuar == True:
