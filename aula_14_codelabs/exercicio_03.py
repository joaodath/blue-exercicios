# Faça um programa com uma função chamada somaImposto. A função possui dois 
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em 
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o 
# valor de custo para incluir o imposto sobre vendas.
#Definidindo Funções
def somaImposto(taxaImposto, custo):
    taxaImposto = taxaImposto.strip().replace('%', '')
    taxaImposto = int(taxaImposto) / 100
    custo = custo.strip().replace('R$', '')
    custo = float(custo)
    custo_com_imposto = custo + (custo * taxaImposto)
    return custo_com_imposto
#Programa Principal
taxa_imposto = input('Informe a taxa de imposto em porcentagem. Exemplo: 32%. ')
custo = input('Informe o valor para ser aplicado o imposto em REAL. Exemplo: R$350.00. ')
calculo_imposto = somaImposto(taxa_imposto, custo)
print(f'''
O valor inicial informado foi: R${custo}.
A taxa de imposto foi: {taxa_imposto}%.
O valor com imposto é: R${calculo_imposto:.2f}.''')
