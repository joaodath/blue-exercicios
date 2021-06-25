# Faça um programa, com uma função que necessite de um argumento. A função retorna 
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for 
# negativo e ‘0’ se for 0.
#Definindo funções
def pos_or_neg(arg1):
    if arg1 > 0:
        return 'P'
    elif arg1 < 0:
        return 'N'
    else:
        return '0'
#Programa Principal
valor1 = float(input('Informe um número inteiro ou decimal para ser verificado: '))
verifica_valor1 = pos_or_neg(valor1)
print(verifica_valor1)