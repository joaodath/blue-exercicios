# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota   Conceito
# >=9.0  A
# >=8.0  B
# >=7.0  C
# >=6.0  D
# >4.0   E
# <=4.0  F
#Definindo funções
def conceito_nota(nota):
    conceito = ''
    if nota >= 9.0:
        conceito = 'A'
        return conceito
    elif nota >= 8.0:
        conceito = 'B'
        return conceito
    elif nota >= 7.0:
        conceito = 'C'
        return conceito
    elif nota >= 6.0:
        conceito = 'D'
        return conceito
    elif nota > 4.0:
        conceito = 'E'
        return conceito
    elif nota <= 4.0:
        conceito = 'F'
        return conceito
#Programa Principal
nota = float(input('Informe a nota do estudante: '))
conceito = conceito_nota(nota)
print(f'O conceito do estudante é {conceito}')