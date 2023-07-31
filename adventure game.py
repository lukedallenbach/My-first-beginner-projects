
def my_own_adventure_game():
    print('Hello!!! Thanks for trying this little game out yo!!!')
    user = input("What's your name yo?\n")
    print(f'\nWelcome, {user}, to this game.')
    print('This game will be a little like a survial game, with each choice changing the outcome of the game.')

    
    def characters_in_the_game():
        character_choices = [
                            'Billy',
                            'Sarah',
                            'Mandy',
                            'Austin'
                             ]
        print('\nPlease choose a character, this will not affect the game, just giving you the option to choose :)')
        print('The character options are below:')
        print(character_choices)
        user_character = input('Who would you like to be?\n')
        print(f'Awesome, so {user}, you chose {user_character}!')
        character_choices.remove(user_character)
        print(f"So it's you, {', '.join(character_choices)} left in the game!")
        #the ', '.join() concatenates the remaining character names into a string separated by a ',' because i am modifying the original list
        print(f"Okay {user_character}, let's get started!!")


        def story_1():
            print(f'\nWe start the game inside a haunted and abandoned hospital. You, along with {character_choices}, all are in the what seems to be the lobby area')
            print("Suddenly, out of no where, there's a scream echoing throughout the halls!!")
            print("The person screaming is begging for help!")
            print("Everybody runs the what seems to be the source of the scream. You all get to a small room and find a tape recorder in the center of the floor.")
            print("You play the tape to here this:\n'I have watched you all for a while now and have decided to kill all but one of you.")
            print("I have set up tricks and traps along the way. Your decisions and choices will dictate if you live or die!! Good Luck, you'll need it!'")
    

        story_1()


    characters_in_the_game()

    def choice_1():
        print('You and the others leave the room towards the hallway. Instead of seeing a hallway, there is a wall replacing the right side.')
        print('The only direction to go is left.')
        print('You and the others turn left and begin to walk. You are all greeted by a light shining into a room.')
        print("The light illuminates the room to show a person tied up and yelling for help.")
        print('Do you help them? ')
        player_choice_1 = input('Which would you choose, yes or no?\n')
        player_choice_1_lower = player_choice_1.lower()
        if player_choice_1_lower == 'no':
            print('This may come back to haunt you later.')
        if player_choice_1_lower == 'yes':
            print('This may help you in the future')
    choice_1()


my_own_adventure_game()
