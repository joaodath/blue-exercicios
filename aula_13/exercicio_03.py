# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.
def som_func(n1 = 0, n2 = 0, n3 = 0):
    somando = n1 + n2 + n3
    soma_resultado = [somando]
    return somando
def media_func(n1 = 0, n2 = 0, n3= 0):
    num = som_func(n1, n2, n3)
    media_resultado = num / 3
    return media_resultado
# def media_func(n):
#     num_de_itens: len(n)
#     media_resultado = n / num_de_itens
#Programa
n1 = int(input('Informe o valor 01: '))
n2 = int(input('Informe o valor 02: '))
n3 = int(input('Informe o valor 03: '))
soma = som_func(n1, n2, n3)
media = media_func(n1, n2, n3)
print(f'''
A soma dos valores informados é: {soma}.

A média dos vaores informados é: {media}''')