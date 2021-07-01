#Faça um programa, com uma função que necessite de três argumentos, e que forneça a 
#soma desses três argumentos.

def soma(n1, n2, n3):
    resultado = n1 + n2 + n3 
    return resultado

numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
numero3 = int(input('Digite o número 3: '))
resultado_da_soma = soma(numero1, numero2, numero3)
resultado_da_soma = numero1 + numero2 + numero3
print(f' O resultado da soma: {resultado_da_soma}')