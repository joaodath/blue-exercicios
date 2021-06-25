# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 
# 1,68 e pese 75kg
#É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
#Definindo funções
def imc_func(peso, altura):
    imc_resultado = peso / altura ** 2
    return imc_resultado
#Programa Principal
print('Este programa irá calcular o seu IMC.')
print()
peso = float(input('Informe o seu peso em kg. Exemplo: 20kg ').strip().replace('kg', '').replace('KG', '').replace('Kg', '').replace('kG', ''))
altura = float(input('Informe a sua altura em metros. Exemplo: 1.78m ').strip().replace('m', '').replace('M', '').replace('mt', '').replace('MT', '').replace('Mt', '').replace('mT', ''))
imc_usuario = imc_func(peso, altura)
print()
# print(f'Seu IMC é igual a: {imc_usuario:.1f}.')
if imc_usuario < 16:
	print(f'Seu IMC é {imc_usuario} e é classificado como Subpeso Severo.')
elif 16 <= imc_usuario <= 19.9:
	print(f'Seu IMC é {imc_usuario} e é classificado como Subpeso.')
elif 20 <= imc_usuario <= 24.9:
	print(f'Seu IMC é {imc_usuario} e é classificado como Normal.')
elif 25 <= imc_usuario <= 29.9:
	print(f'Seu IMC é {imc_usuario} e é classificado como Sobrepeso.')
elif 30 <= imc_usuario <= 29.9:
	print(f'Seu IMC é {imc_usuario} e é classificado como Obeso.')
else:
	print(f'Seu IMC é {imc_usuario:.1f} e é classificado como Obeso Mórbido.')