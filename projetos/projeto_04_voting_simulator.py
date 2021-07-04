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
                'candidate1_name': 'Candidate 1',
                'candidate2_name': 'Candidate 2',
                'candidate3_name': 'Candidate 3',
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
        return 'YOU CANNOT VOTE. YOU\'RE TOO YOUNG!'
        
    elif auth.strip().upper() == 'SHOW' and vote == 0 or '0':
        total_valid_votes = sum(candidates['candidate1']) + sum(candidates['candidate2']) + sum(candidates['candidate3'])
        non_valid_votes = sum(candidates['null']) + sum(candidates['blank'])

        if sum(candidates['candidate1']) > sum(candidates['candidate2']) and sum(candidates['candidate1']) > sum(candidates['candidate3']):
            elected = candidates['candidate1_name']
            elected_votes = sum(candidates['candidate1'])
            return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)
        
        elif sum(candidates['candidate2']) > sum(candidates['candidate1']) and sum(candidates['candidate2']) > sum(candidates['candidate3']):
            elected = candidates['candidate2_name']
            elected_votes = sum(candidates['candidate2'])
            return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)
        
        elif sum(candidates['candidate3']) > sum(candidates['candidate1']) and sum(candidates['candidate3']) > sum(candidates['candidate2']):
            elected = candidates['candidate3_name']
            elected_votes = sum(candidates['candidate3'])
            return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)
        
        elif sum(candidates['candidate1']) == sum(candidates['candidate2']) or sum(candidates['candidate1']) == sum(candidates['candidate3']) or sum(candidates['candidate2']) == sum(candidates['candidate3']):
            if sum(candidates['candidate1']) == sum(candidates['candidate2']) and sum(candidates['candidate3']) == 0:
                elected = ''
                elected_votes = 0
                return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)
            
            elif sum(candidates['candidate1']) == sum(candidates['candidate3']) and sum(candidates['candidate2']) == 0:
                elected = ''
                elected_votes = 0
                return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)

            elif sum(candidates['candidate2']) == sum(candidates['candidate3']) and sum(candidates['candidate1']) == 0:
                elected = ''
                elected_votes = 0
                return scoreboard(total_valid_votes, non_valid_votes, elected, elected_votes)         

def scoreboard(valid_votes, invalid_votes, elected_name, elected_total_votes):
    #There are no calculations done here. Only optimizing the code for less lines
    total_valid_votes = valid_votes
    non_valid_votes = invalid_votes
    elected = elected_name
    elected_votes = elected_total_votes
    print_elected = ''
    if elected == '': 
        print_elected = 'There was a tie. Nobody won!'
    else:
        print_elected = f'{elected} was elected with a total of {elected_votes} valid votes.'
    return f'''
            ---------------------------------------------------------------
            Scoreboard for {year_now} election.
            ---------------------------------------------------------------

            {candidates['candidate1_name']}: {sum(candidates['candidate1'])}
            {candidates['candidate2_name']}: {sum(candidates['candidate2'])}
            {candidates['candidate3_name']}: {sum(candidates['candidate3'])}
            Nulled Votes: {sum(candidates['null'])}
            Blank Votes: {sum(candidates['blank'])}
            Total Valid Votes: {total_valid_votes}
            Total Non-valid Votes: {non_valid_votes}

            ---------------------------------------------------------------

            {print_elected}

            '''

#Main Program
#Attention: Since we're simulating an election software, I've created a second dimension for this exercise: once started, the software will first look for the officer password. In this case, I've set the password as 'blue'. =D
#Cleaning the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
from time import sleep
print('''
Hello, Officer! Welcome to the Voting System!
Waiting for iniatilization. ''')
password = str(input('Please, inform your password: ').strip().lower())
while password != 'blue':
    password = str(input('Please, inform your password: ').strip().lower())
if password == 'blue':
    print(f'''
        Welcome, officer!
        The candidates available are:
        --------------------------------
        [1] {candidates['candidate1_name']}
        [2] {candidates['candidate2_name']}
        [3] {candidates['candidate3_name']}
        ''')
    change = str(input('Do you wanna change their names? Y/N ').strip().upper())
    while change[0] not in ['Y', 'N']:
        change = str(input('I\'m sorry! I didn\'t get that. Do you wanna change their names? Y/N ').strip().upper())
    if change.startswith('Y'):
        candidates['candidate1_name'] = str(input('Inform the name for Candidate 1: ').strip().capitalize())
        candidates['candidate2_name'] = str(input('Inform the name for Candidate 2: ').strip().capitalize())
        candidates['candidate3_name'] = str(input('Inform the name for Candidate 3: ').strip().capitalize())
    else:
        pass
    print('Okay. The system is ready!')
    sleep(1)
    print('Rebooting in 3...')
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Rebooting in 2...')
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Rebooting in 1...')
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Rebooting...')
    os.system('cls' if os.name == 'nt' else 'clear')
#Voting starts here
keep_voting = True
while keep_voting == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
        Hello! Welcome to the Voting System!
        The candidates available are:
        -----------------------
        [1] {candidates['candidate1_name']}
        [2] {candidates['candidate2_name']}
        [3] {candidates['candidate3_name']}
        [4] Null Vote
        [5] Blank Vote
        ''')
    year_of_birth = int(input('In order to vote, please, inform your year of birth: '))
    while year_of_birth < 1903:
        year_of_birth = int(input('It seems like you\'re a bit too old, huh? In order to vote, please, inform your year of birth: '))
    authorization = autoriza_voto(year_of_birth)
    print()
    vote_number = int(input('Now, inform the number of your candidate: '))
    vote_process = votacao(authorization, vote_number)
    print()
    print(vote_process)
    keep_voting_ask = str(input('Close voting? Y/N ').strip().upper())
    while keep_voting_ask[0] not in ['Y', 'N']:
        keep_voting_ask = str(input('Close voting? Y/N ').strip().upper())
    if keep_voting_ask.startswith('Y'):
        password = str(input('Please, inform your officer\'s password: ').strip().lower())
        if password == 'blue':
            keep_voting = False
        else:
            print('Password Incorrect.')
            sleep(3)
            keep_voting_ask = True
    else:
        sleep(3)
        keep_voting = True
print()
print('Closing voting.')
sleep(1)
print()
print('Calculating data.')
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print()
print(votacao('SHOW', 0))