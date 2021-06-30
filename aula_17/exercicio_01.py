# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica.
#Defining Classes
from random import randint
class Dice:
    def __init__(self):
        self.shownf = self.roll()
    def roll(self):
        dice = randint(1,6)
        self.shownf = dice
        return self.shownf
    def shown(self):
        return self.shownf

class Coin:
    def __init__(self):
        self.shownf = self.flip()
    def flip(self):
        face = randint(1,2)
        if face == 1:
            self.shownf = 'heads'
            return self.shownf
        else:
            self.shownf = 'tails'
            return self.shownf
    def shown(self):
        return self.shownf


#Main Program
from time import sleep
print('Hello, fellow passenger!')
sleep(1)
print('What an interesting turn of events to find you here.')
sleep(1)
print('Would you be interested in a game of dices or coins? You may not say \'no\'!')
sleep(2)
print('Shall we begin?')
sleep(1)
# person1 = ''
choice_person1 = str(input('Would you like to roll the dice or flip the coin? Type DICE or COIN: ').strip().upper())
if choice_person1.startswith('D'):
    print('Let\'s roll this dice!')
    person1 = Dice()
    sleep(1)
    print(f'You got {person1.shown()} on your dice.')
elif choice_person1.startswith('C'):
    print('Let\'s flip this coin!')
    person1 = Coin()
    person1.shownf = person1.flip()
    sleep(1)
    print(f'You got {person1.shown()} on your coin.')
else:
    sleep(1)
    print('It seems like you don\'t know how to play games.')
print('End of game. You\'re free to go.')
    
    

