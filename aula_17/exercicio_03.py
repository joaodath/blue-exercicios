# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela
# menor que 21 anos, ela deve crescer 0,5 cm
from time import sleep
#Cleaning the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
#Importing datetime to check the actual year
import datetime
now = datetime.datetime.now()
year_now = now.year
#Defining classes
class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight #described in kg
        self.height = height #described in cm
    def old(self, year1):
        if year1 > year_now:
            year = year1 - year_now
            if self.age < 21:
                growth = year * 0.5
                self.height += growth
                self.age += year
            else:
                self.age += year
            return self.age
        else:
            return None
    def fatten(self, weight2):
        self.weight += weight2
        return self.weight
    def lose_weight(self, weight3):
        self.weight -= weight3
        return self.weight
    def grow(self, height2):
        self.height += height2
        return self.height


#Main Program
print('''
Hello! Let's play \'Fuck Someone\'s Life!
For this game, you must select one of the options.
Now, enough of this. Let's play!''')
sleep(1)
play_game = play_another_game = True #Control variables for while loops ahead
#Here is the actual game. The first while loop controls how much peoples'lives the player will fuck
while play_another_game == True:
    play_game = True #Sets the control variable for the while loop of the menu to true because if someone stops the while loop ahead in the code setting this to False, the outer while loop will set it to true again and the program will not break
    name = str(input('What is the person name? ').strip().capitalize())
    age = int(input(f'What is the age of {name}? '))
    weight = float(input(f'What is the weight of {name}? '))
    height = float(input(f'What is the height of {name} in centimeters (cm)? Example: 175.5cm '))
    person1 = Person(name, age, weight, height)
    print()
    #Now that we know the person details, we print the menu for the game
    while play_game == True:
        print(f'''
            ----------------------------------------
            Okay, these are your options for {name}:
            [1] Gain Weight
            [2] Lose Weight
            [3] Calculate how old they will be when a year you inform has come.''')
        print()
        choice = int(input('Please, select an option: '))
        while choice not in [1, 2, 3]: #checks if the player chose a correct option or gives the option to try again until it is correct
            print()
            choice = int(input('Wrong option. Please try again: '))
        if choice == 1:
            new_weight = float(input('Please inform the gained weight in kilograms. Example: 62.5 '))
            new_weight_type = str(type(new_weight)) #Checks the class of the variable and stores it as string to compare in the while loop ahead and use as control variable. I still need to treat the error if the player inputs a str or int or any other datatype
            while new_weight_type != "<class 'float'>":
                print()
                new_weight = float(input('Wrong weight. Please try again: '))
                new_weight_type = str(type(new_weight))
            person1.fatten(new_weight)
            print(f'''
            {person1.name} has gained {new_weight}kg.
            Their new weight is {person1.weight}kg.''')
        elif choice == 2:
            new_weight = float(input('Please inform the gained weight in kilograms. Example: 62.5 '))
            new_weight_type = str(type(new_weight)) #Checks the class of the variable and stores it as string to compare in the while loop ahead and use as control variable. I still need to treat the error if the player inputs a str or int or any other datatype
            print(new_weight_type)
            while new_weight_type != "<class 'float'>":
                print()
                new_weight = float(input('Wrong weight. Please try again: '))
                new_weight_type = str(type(new_weight))
            person1.lose_weight(new_weight)
            print(f'''
            {person1.name} has lost {new_weight}kg.
            Their new weight is {person1.weight}kg.''')
        elif choice == 3:
            new_year = int(input(f'''
                            Please inform the year to calculate {person1.name} new age: '''))
            while new_year < year_now or new_year == year_now: #Checks to see if the new year is in the past or is the exact same year as of now, in which cases the age would regress
                new_year = int(input(f'''
                                I'm sorry. As of this time, TARDIS matrix are unavailable.
                                Therefore, our time machines are not accessible for trips back in time. Please, try again.
                                Please inform the year to calculate {person1.name} new age: '''))
            person1.old(new_year)
            print(f'''
                    {person1.name} has aged {new_year - year_now} years.
                    They are now {person1.age} years old. ''')
        #The menu while loop is almost over now
        print('''
        So, this is it. This is the end.
        Hold your breath and count to ten.''')
        sleep(2)
        print('''
        Okay, just foolin\' around with ya.''')
        #Asks the player if they still wanna fuck the same person's life
        play_game_ask = str(input(f'''
        Wanna keep playing? Y/N ''').strip().upper())
        #the while loop below runs until the player informs the correct option
        while play_game_ask.startswith('Y') != True and play_game_ask.startswith('N') != True:
            play_game_ask = str(input(f'''
                                Ops, wrong option. Try again.
                                Wanna keep playing? Y/N ''').strip().upper())
        if play_game_ask.startswith('Y'):
            play_game = True
        else:
            play_game = False
    #Asks the player if they wanna fuck the somebody else's life if not, it ends the game
    play_another_game_ask = str(input('Wanna fuck somebody else\'s life? Y/N ').strip().upper())
    #the while loop below runs until the player informs the correct option
    while play_another_game_ask.startswith('Y') != True and play_another_game_ask.startswith('N') != True:
            play_another_game_ask = str(input(f'''
                                Ops, wrong option. Try again.
                                Wanna keep playing? Y/N ''').strip().upper())
    if play_another_game_ask.startswith('Y'):
        play_another_game = True
    else:
        play_another_game = False
print('End of game. Come back soon!')