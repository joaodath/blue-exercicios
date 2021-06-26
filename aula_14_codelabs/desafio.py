# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no 
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que 
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro 
# terá 29 dias
#Anos divisíveis por 4 são bissextos
#Declaring functions
#Função pensada por mim
# def written_month_func(date):
#     # given_date = [date]
#     day = date[0:2]
#     month = date[3:5]
#     year = date[6:10]
#     month1 = ''
#     if month == '01':
#         month1 = 'Janeiro'
#     elif month == '02' and day != '29':
#         month1 = 'Fevereiro'
#     elif month == '3':
#         month1 = 'Março'
#     elif month == '4':
#         month1 = 'Abril'
#     elif month == '5':
#         month1 = 'Maio'
#     elif month == '6':
#         month1 = 'Junho'
#     elif month == '7':
#         month1 = 'Julho'
#     elif month == '8':
#         month1 = 'Agosto'
#     elif month == '9':
#         month1 = 'Setembro'
#     elif month == '10':
#         month1 = 'Outubro'
#     elif month == '11':
#         month1 = 'Novembro'
#     elif month == '12':
#         month1 = 'Dezembro'
#     return f'{day} de {month1} de {year}'
#Função do Victor Fernando
def mes_escrito(value): #DD/MM/AAAA
    dia = value[0:2]
    dia_chave = int(dia)
    mes_chave = value[3:5]
    ano = value[6:10]
    ano_valida = int(ano)
    mes={"01":"janeiro" ,"02":"fevereiro", "03":"março","04":"abril","05":"maio","06":"junho",
"07":"julho","08":"agosto", "09":"setembro", "10":"outubro", "11":"novembro", "1n2":"dezembro"}
    if mes[mes_chave] == 'fevereiro' and dia_chave <= 29 and ano_valida // 4 == 0:
        return f'{dia} de {mes[mes_chave]} de {ano}'
    elif mes[mes_chave] != 'fevereiro' and dia_chave <= 31:
        return f'{dia} de {mes[mes_chave]} de {ano}'
    elif mes[mes_chave] == 'fevereiro' and dia_chave <= 28:
        return f'{dia} de {mes[mes_chave]} de {ano}'
    else:
        return None 
#Main Program
data_informada = input('Informe uma data no formato DD/MM/AAAA: ')
data_escrita = mes_escrito(data_informada)
print(data_escrita)



