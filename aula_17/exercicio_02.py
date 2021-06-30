# #01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# # programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# # quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# # dicionário, incluindo o total de gols feitos durante o campeonato.

# player_data = dict()
# goals_temp_list = list()
# name = str(input('Please, inform the player\'s name: ').strip().capitalize())
# games = int(input(f'Now, inform the number of games {name} participated in: '))
# for c in range(games):
#     goals = int(input(f'Please, inform the number of goals made during the {c+1}° game of {name}: '))
#     goals_temp_list.append(goals)
# #Building the dictionary
# player_data['name'] = name
# player_data['games'] = games
# player_data['goals'] = goals_temp_list
# player_data['total_goals'] = sum(goals_temp_list)
# #Printing the dictionary
# print(player_data)

# Vamos aprimorar o código: cadastro de jogador de futebol.py que foi
# desenvolvido no Code Lab da aula 14. Faça com que o seu código
# funcione para vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento de cada jogador.

class Player:
    def __init__(self, name, games, goals):
        self.name = name
        self.games = games
        self.goals = goals
        self.total_goals = sum(goals)
    def prod(self):
        productivity = self.total_goals / self.games
        return productivity
    def print_prod(self):
        productivity = self.total_goals / self.games
        return f'''
                Productivity Scoreboard for Player {self.name}
                ---------------------------------------------
                Total Games: {self.games}
                Total Goals: {self.total_goals}
                Goals per Game: {productivity}'''

#Main Program
goals_temp_list = list()
name = str(input('Please, inform the player\'s name: ').strip().capitalize())
games = int(input(f'Now, inform the number of games {name} participated in: '))
for c in range(games):
    goals = int(input(f'Please, inform the number of goals made during the {c+1}° game of {name}: '))
    goals_temp_list.append(goals)
#Passing the data back to an object
player1 = Player(name, games, goals_temp_list)
#Print the scoreboard
print(player1.print_prod())