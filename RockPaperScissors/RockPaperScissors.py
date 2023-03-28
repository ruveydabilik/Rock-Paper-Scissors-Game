#Importing the random library
import random

#A list containing the three actions of the game.
actions = ['Rock', 'Paper', 'Scissors']

#Settings the scores to 0
pc_score = 0 #score of the computer
player_score = 0 #score of the player

#Asking the player how many rounds s/he wants to play
round = input('How many round do you want to play ?:')

for i in range(1, int(round)+1):

    #Selecting a random action for computer
    pc_action = actions[random.randint(0,2)]

    player_action = input("What's your choice? 'R' for Rock, 'P' for Paper, 'S' for Scissors\n")
    player_action = player_action.upper()

    if player_action == 'R':
        player_action = 'Rock'
    elif player_action == 'P':
        player_action = 'Paper'
    elif player_action == 'S':
        player_action = 'Scissors'
    else:
        while player_action != 'R' or player_action !='P' or player_action !='S':
            player_action = input('Please enter R, P or S!\n')
            player_action = player_action.upper()
            if player_action == 'R' or player_action == 'P' or player_action == 'S':
                if player_action == 'R':
                    player_action = 'Rock'
                elif player_action == 'P':
                    player_action = 'Paper'
                elif player_action == 'S':
                    player_action = 'Scissors'
                break;

    print('Computer: ', pc_action)
    print('You: ', player_action)

    #Adding the tie condition and the remaining conditions
    if pc_action == player_action:
        print('Tie! Both players chose the same action.\n')
    elif pc_action == 'Rock' and player_action == 'Paper':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Paper' and player_action == 'Rock':
        print('Computer won the round\n')
        pc_score += 1
    elif pc_action == 'Rock' and player_action == 'Scissors':
        print('Computer won the round\n')
        pc_score += 1
    elif pc_action == 'Scissors' and player_action == 'Rock':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Paper' and player_action == 'Scissors':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Scissors' and player_action == 'Paper':
        print('Computer won the round\n')
        pc_score += 1
    else:
        print('Something went wrong!\n')

    print('Current situation:')
    print('Computer : ', pc_score)
    print('You : ', player_score)

"""
#For loop can be converted into while loop like in here:

while True:

#Selecting a random action for computer
    pc_action = actions[random.randint(0,2)]

    player_action = input("What's your choice? 'R' for Rock, 'P' for Paper, 'S' for Scissors\n")
    player_action = player_action.upper()

    if player_action == 'R':
        player_action = 'Rock'
    elif player_action == 'P':
        player_action = 'Paper'
    elif player_action == 'S':
        player_action = 'Scissors'
    else:
        while player_action != 'R' or player_action !='P' or player_action !='S':
            player_action = input('Please enter R, P or S!\n')
            player_action = player_action.upper()
            if player_action == 'R' or player_action == 'P' or player_action == 'S':
                if player_action == 'R':
                    player_action = 'Rock'
                elif player_action == 'P':
                    player_action = 'Paper'
                elif player_action == 'S':
                    player_action = 'Scissors'
                break;

    print('Computer: ', pc_action)
    print('You: ', player_action)

    #Adding the tie condition and the remaining conditions
    if pc_action == player_action:
        print('Tie! Both players chose the same action.\n')
    elif pc_action == 'Rock' and player_action == 'Paper':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Paper' and player_action == 'Rock':
        print('Computer won the round\n')
        pc_score += 1
    elif pc_action == 'Rock' and player_action == 'Scissors':
        print('Computer won the round\n')
        pc_score += 1
    elif pc_action == 'Scissors' and player_action == 'Rock':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Paper' and player_action == 'Scissors':
        print('You won the round\n')
        player_score += 1
    elif pc_action == 'Scissors' and player_action == 'Paper':
        print('Computer won the round\n')
        pc_score += 1
    else:
        print('Something went wrong!\n')

    print('Current situation:')
    print('Computer : ', pc_score)
    print('You : ', player_score)

    answer = input('Do you want to continue ? (Y: to continue or N: to stop):')
    if(answer == 'N' ):
        break;
"""

#Printing the score
print()
print('Last situation:')
print('Computer : ', pc_score)
print('You : ', player_score)

if pc_score > player_score:
    print('Computer won the game')
elif player_score > pc_score:
    print('You won the game. Congratulations!')
else:
    print('Tie! Nobody won')
