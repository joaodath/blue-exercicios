# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles 
# forem iguais, imprima que eles são iguais.
#Declaring functions
def which_size(value1, value2):
    if value1 == value2:
        return f'O valor {value1} é igual ao valor {value2}.'
    elif value1 > value2:
        return f'O valor menor é {value2}.'
    else:
        return f'O valor menor é {value1}.'
#Main Program
value1 = int(input('Informe o valor 1: '))
value2 = int(input('Informe o valor 2: '))
result = which_size(value1, value2)
print(result)