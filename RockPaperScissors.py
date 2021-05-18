import random
from enum import IntEnum


class Choice(IntEnum):
    rock = 0
    paper = 1
    scissors = 2 



def get_player_choice():
    
    #possible_choices = ['rock'[0], 'paper'[1], 'scissors'[2]]
    # computer_choice = random.choice(possible_choices)
    # print(f'You chose {player_choice}. The computer chose {computer_choice}.')
    #INSTEAD OF ABOVE --->
    #simplify with list comprehension - to not have to add choices later on.. 
    choices = [f'{choice.name}[{choice.value}]' for choice in Choice]
    choices_string = ','.join(choices)
    player_choice = int(input(f'Choose one:({choices_string}): '))
    choice = Choice(player_choice)
    return choice 

def get_computer_choice():
    #returns a random num in range 0 - 2 
    computer_choice = random.randint(0, len(Choice) - 1)
    choice = Choice(computer_choice)
    return choice 

# def rock_paper_scissors_shoot(player_choice, computer_choice):

#     if player_choice == computer_choice:
#         print(f'You AND computer chose {player_choice.name} it is a TIE. Try again.')
#     elif player_choice == Choice.rock:
#         if computer_choice == Choice.scissors:
#             print('Rock slams scissors. YOU WIN!')
#         else: 
#             print('Paper engulfs rock. YOU LOSE!')
#     elif player_choice == Choice.paper:
#         if computer_choice == Choice.rock:
#             print('Paper engulfs rock. YOU WIN!')
#         else: 
#             print('Scissors slice paper. YOU LOSE!')
#     elif player_choice == Choice.scissors:
#         if computer_choice == Choice.paper:
#             print('Scissors slice paper. YOU WIN')
#         else: 
#             print('Rock slams scissors. YOU LOSE!')


###################Instead of above code you can simply with dictionaries key-value pair relationships. key = choice value = list of other choices it thwarts#######################
def rock_paper_scissors_shoot(player_choice, computer_choice):
    wins = {
        Choice.rock: [Choice.scissors], # Rock slams scissors
        Choice.paper: [Choice.rock], #Paper engulfs rock
        Choice.scissors: [Choice.paper] #Scissors slice paper 
    }
    loses = wins[player_choice]
    if player_choice == computer_choice:
        print(f'You AND computer chose {player_choice.name}. It is a TIE. Try again.')
    elif computer_choice in loses:
        print(f'{player_choice.name} thwacks {computer_choice.name}: YOU WIN!')
    else:
        print(f'{computer_choice.name} thwacks {player_choice.name}: YOU LOSE! Better luck next time!')


while True:
    try:
        player_choice = get_player_choice()
    except ValueError as e:
        range_string = f'[0, {len(Choice) - 1 }]'
        print(f'Invalid choice. Please choose a value in the range of {range_string}')
        continue

    computer_choice = get_computer_choice()
    rock_paper_scissors_shoot(player_choice, computer_choice)

    play_another_round = input('play another round? y/n: ')
    if play_another_round != 'y':
        print('Thanks for playing! See you next time')
        break 

