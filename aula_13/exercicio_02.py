#Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def pos_or_neg(n):
    n = int(n)
    if n > 0:
        return 'P'
    else:
        return 'N'

num = pos_or_neg(int(input('Informe o número: ')))
print(num)

