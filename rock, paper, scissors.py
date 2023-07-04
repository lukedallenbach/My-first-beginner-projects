

# the length of the game can be changed by changing the number in the second function call 

def rock_paper_scissors_game(x):
    import random 
    computer_options = ['rock', 'paper', 'scissors']
    computer_score = 0
    human_score = 0
    print('Wlecome to my rock, paper scissors game.')
    print('The rules are very simple. Choose either rock, paper, or scissors.')
    print(f'The aim is to beat the computer to {x} points. A point is gained by either the computer or you by beating the other players hand.')
    print('Good luck yo')

    while human_score < x and computer_score < x:
        my_hand = input('\nPlease choose either rock, paper, or scissors: ')
        computer_hand = random.choice(computer_options)
        
        if my_hand == 'rock':
            if computer_hand == 'paper':
                computer_score += 1
                print('Paper beats rock, computer wins a point.')
            elif computer_hand == 'scissors':
                human_score += 1
                print('Rock beats scissors, you win a point.')
            else:
                print('It\'s a tie!')
        
        elif my_hand == 'paper':
            if computer_hand == 'scissors':
                computer_score += 1
                print('Scissors beats paper, computer wins a point.')
            elif computer_hand == 'rock':
                human_score += 1
                print('Paper beats rock, you win a point.')
            else:
                print('It\'s a tie!')
        
        elif my_hand == 'scissors':
            if computer_hand == 'rock':
                computer_score += 1
                print('Rock beats scissors, computer wins a point.')
            elif computer_hand == 'paper':
                human_score += 1
                print('Scissors beats paper, you win a point.')
            else:
                print("It's a tie yo!")
        else:
            print('Invalid input. Please choose either rock, paper, or scissors dummy.')
            
        print(f'You have {human_score} points and the computer has {computer_score} points.')
    
    print(f'The final score is {human_score} points for you and {computer_score} for the computer.')
    
    if human_score > computer_score:
        print('Nice job yo, you won!')
    else:
        print('Good try but beating a computer is hard :/')
    
rock_paper_scissors_game(2)



