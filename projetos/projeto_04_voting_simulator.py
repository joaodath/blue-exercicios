# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação
# if 18 <= idade < 70:
#         return f'Idade: {idade} - Voto Obrigatório'
#     elif 16 <= idade < 18 or idade >= 70:
#         return f'Idade: {idade} - Voto Opcional'
#     else:
#         return f'Idade: {idade} - Voto Negado'
#Setting the current year
import datetime
now = datetime.datetime.now()
year_now = now.year
#Declaring dictionary needed INSIDE the functions
candidates = {  'candidate1': list(),
                'candidate2': list(),
                'candidate3': list(),
                'null': list(),
                'blank': list()
            }
#Defining Functions
def autoriza_voto(born_year):
    if born_year < year_now:
        age = year_now - born_year
        if 18 <= age < 70:
            return 'OBRIGATÓRIO'
        elif 16 <= age < 18 or age >= 70:
            return 'OPCIONAL'
        else:
            return 'NEGADO'
    elif born_year >= year_now:
        return None
def votacao(auth, vote):
    if auth.strip().upper() == 'OBRIGATÓRIO' or auth.strip().upper() == 'OPCIONAL':
        if vote == 1 or vote == '1':
            candidates['candidate1'].append(1)
            return 'YOU VOTED!'
        elif vote == 2 or vote == '2':
            candidates['candidate2'].append(1)
            return 'YOU VOTED!'
        elif vote == 3 or vote == '3':
            candidates['candidate3'].append(1)
            return 'YOU VOTED!'
        elif vote == 4 or vote == '4':
            candidates['null'].append(1)
            return 'YOU VOTED!'
        elif vote == 5 or vote == '5':
            candidates['blank'].append(1)
            return 'YOU VOTED!'
        else:
            candidates['null'].append(1)
            return 'NO CANDIDATES FOR THIS NUMBER. YOUR VOTE IS NOW NULLED.'
    elif auth.strip().upper() == 'NEGADO':
        return 'YOU CANNOT VOTE'
    elif auth.strip().upper() == 'SHOW' and vote == 0 or '0':
        total_votes = sum(candidates['candidate1']) + sum(candidates['candidate2']) + sum(candidates['candidate3'])
        non_valid_votes = sum(candidates['null']) + sum(candidates['blank'])
        if sum(candidates['candidate1'])/total_votes > sum(candidates['candidate2'])/total_votes and sum(candidates['candidate1'])/total_votes > sum(candidates['candidate3'])/total_votes:
            elected = 'Candidate 1'
            elected_votes = sum(candidates['candidate1'])
        elif sum(candidates['candidate2'])/total_votes > sum(candidates['candidate1'])/total_votes and sum(candidates['candidate2'])/total_votes > sum(candidates['candidate3'])/total_votes:
            elected = 'Candidate 2'
            elected_votes = sum(candidates['candidate2'])
        elif sum(candidates['candidate3'])/total_votes > sum(candidates['candidate1'])/total_votes and sum(candidates['candidate3'])/total_votes > sum(candidates['candidate2'])/total_votes:
            elected = 'Candidate 3'
            elected_votes = sum(candidates['candidate3'])
        return f'''
                ---------------------------------------------------------------
                Scoreboard for {year_now} election.
                ---------------------------------------------------------------

                Candidate 1: {sum(candidates['candidate1'])}
                Candidate 2: {sum(candidates['candidate2'])}
                Candidate 3: {sum(candidates['candidate3'])}
                Nulled Votes: {sum(candidates['null'])}
                Blank Votes: {sum(candidates['blank'])}
                Total Valid Votes: {total_votes}
                Total Non-valid Votes: {non_valid_votes}

                ---------------------------------------------------------------

                Elected: {elected} with a total of {elected_votes} valid votes.

                '''
    else:
        return None
#Cleaning the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
from time import sleep

keep_voting = True
while keep_voting == True:
    year_of_birth = int(input('Please, inform your year of birth: '))
    authorization = autoriza_voto(year_of_birth)
    print()
    vote_number = int(input('Please, inform the number of your candidate: '))
    vote_process = votacao(authorization, vote_number)
    print()
    print(vote_process)
    keep_voting_ask = str(input('Close voting? Y/N ').strip().upper())
    while keep_voting_ask[0] not in ['Y', 'N']:
        keep_voting_ask = str(input('Close voting? Y/N ').strip().upper())
    if keep_voting_ask.startswith('Y'):
        keep_voting = False
    else:
        keep_voting = True
print()
print('Closing voting.')
sleep(1)
print()
print('Calculating data.')
sleep(1)
print()
print(votacao('SHOW', 0))