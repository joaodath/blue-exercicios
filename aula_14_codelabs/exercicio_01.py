#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
#Declarando funções
def soma_func(n1 = 0, n2 = 0, n3 = 0):
    calc_func = n1 + n2 + n3
    return calc_func
#Programa Principal
from random import randint
valor1 = randint(2, 100)
valor2 = randint(2, 100)
valor3 = randint(2, 100)
print('------ Lista de Valores sendo aleatórios de 2 a 100 a serem somados ------')
print(valor1)
print(valor2)
print(valor3)
print('-' *74)
soma = soma_func(valor1, valor2, valor3)
print(f'Resultado da soma: {soma}.')