from __future__ import print_function # use Python 3.0 printing
#has to be up top for the code to work

# Mario_Maze is the second half of the game, but we pasted it here because it is
# falling under the variable called mario_game, which is down below.  mario_game
# is the command which we use to start the whole program
def mario_maze():
    print("Proceed through Browser's maze by typing only",
     "'left' or 'right' for the next FIVE times.")
    guess = str(raw_input('Type: '))

    ''' These are all of the possible choice which someone can make during
    the maze. The second part is where you enter
    to the maze and have to navigate your way out of it.  This part only
    requires left or no right answer.
    '''
    if guess == 'right':
        print("Correct, continue your journey by typing",
        "'left' or 'right'.")
        guess1 = str(raw_input('Type: '))
        if guess1 == 'right':
            print("Correct, onwards.")
            guess2 = str(raw_input('Type: '))
            if guess2 == 'left':
                print("Correct, you rock. Continue by",
                "typing in 'left' or 'right'.")
                guess3 = str(raw_input('Type: '))
                if guess3 == 'right':
                    print("Correct, you are almost there.")
                    guess4 = str(raw_input('Type: '))
                    if guess4 == 'left':
                        print("You have reached Princess",
                        "Peach's room.")
                        print("Congragulations you saved",
                        "her!")
                        print("Game Over")
                        print("Kalra & Vallapureddy 2019")
                    elif guess4 == 'right':
                        print("Wrong Pathway")
                        print("You died")
                        print("Press the up arrow and then",
                        "enter to restart")
                        print("Now you have to do all of",
                        "the castle and maze levels again.")
                        print("Hahaha, we are evil, no",
                        "just Keenan")

                    # Wrong answers for maze options.
                    # Counter solutions shown below.

                    else:
                        print("We don't understand gibberish,",
                            "you died.")
                elif guess3 == 'left':
                    print("Wrong Pathway.")
                    print("You died a horrible death.")
                    print("Press the up arrow and then",
                    "enter to restart.")
                else:
                    print("We don't understand",
                    "you died.")
            elif guess2 == 'right':
                print("Wrong Pathway.")
                print("You died without pain, thankfully.")
                print("Press the up arrow and then",
                "enter to restart")
            else:
                print("We don't understand gibberish,",
                "you died.")
        elif guess1 == 'left':
            print("Wrong Pathway")
            print("You died somehow.")
            print("Press the up arrow and then",
            "enter to restart")
        else:
            print("We don't understand gibberish,",
            "you died.")
    elif guess == 'left':
        print("Wrong Pathway")
        print("You died")
        print("Press the up arrow and then enter",
        "to restart")
    else:
        print("We don't understand gibberish,",
        "you died.")


def mario_game():
    '''This is a text-adventure game in which you have become Mario and have
    to rescue Princess Peach from Bowser.  The game is split in into two
    different parts.  The first part of the game is when you are actually in the
    castleand face real Mario obstacles.  This part of the game is is the where
    it requires actual thought, and is hard. '''

    print('Do you want to play Mario Text Adventure?')
    print("Please type in 'yes' or 'no'.")
    answer = str(raw_input('Type: '))
    if answer == 'no':
        print('Too bad, you have to play!')
    elif answer == 'yes':
        print("Let's get started")
    else:
        print("We do NOT understand gibberish. Only type 'yes' or 'no'")

    print('Quick Disclaimer: This game was created by Keenan Kalra and Nibodh',
    'Vallapureddy in CSP.')
    print('If this game causes any issues, such as driving you',
    'mad, we are not resposible.')
    print('If you feel like punching the computer stop playing immediately!')
    print('PS: If you kill yourself within the first three turns, please stop',
    'playing the game as you are NOT talented enough to be Mario!!')
    print('Anyways here is the game ! Please enjoy the game and have fun'
    '(but not too much).')

    print('Please enter your name')
    print('We prefer that you keep your name Mario, it may or may not help you',
    'through the game...')
    name = str(raw_input('Type: '))

    if name == "mario" or "Mario":
        print("Great, you have unlocked no special abilities...")
        print("Just Kidding")
        print("Type in 'yes' when it asks you whether to enter the door or",
        "not.")

    print('Welcome,', name + '!')
    print("Only you can save Princess Peach from Browser's castle.")
    print("Be careful what you type...it will be game over before you know it.")

    # Start of Bowser's Castle
    ''' These are all of the options for the castle part of the game. '''
    def castle():
        print("Do you want to open the powerup block?")
        print("Type in 'yes' or 'no'.")
        choice = str(raw_input('Type:'))
        if choice == 'yes' or 'no':
            print('You have unlocked fire', name, 'regardless and continue',
            'your journey.')


            print('You are travelling and you meet a goomba.',
            'Do you want to avoid it?')
            print("Type in either 'yes' or 'no.'")
            choice1 = str(raw_input('Type:'))
            if choice1 == 'no':
                print('Good job, you kill the goomba and continue your way.')

                print('As you are moving, you run into a major issue.')
                print('There is a huge lava pit.')
                print('Do you take a running jump or the elevator?')
                print("Type in 'jump' or 'elevator'.")
                choice2 = str(raw_input('Type:'))
                if choice2 == 'elevator':
                    print('Smart boy! There is no way you are making that',
                    'jump.')

                    print('You are almost there. Except now you have see a',
                    'fireball coming at you!')
                    print('Do you want to eat the fireball or dodge it?')
                    print("Type in 'eat' or 'dodge'.")
                    choice3 = str(raw_input('Type:'))
                    if choice3 == 'eat':
                        print('I guess you are really hungry, but it worked',
                        'for you.')

                        print('You are successfully able to continue to the',
                        'final.')
                        print('Here you see a door. Do you want to enter?')
                        print("Type in 'enter' or 'no'")
                        choice4 = str(raw_input('Type:'))
                        if choice4 == 'enter':
                            print('Congragulations! Now you go into the maze.')
                            # Start of the maze

                            mario_maze()
                        # Else statements for Bowser's Castle
                        # The wrong answers for the statments.

                        # This is the choice is for the secret room + secret
                        #hallway
                        elif choice4 == 'no':
                            print('Congragulations, you have entered a secret',
                            'room.')
                            print('Would you like to enter it?')
                            print("Please enter either 'yes' or 'no'")
                            room_choice = str(raw_input('Type: '))
                            print("Hahaha, you made the wrong choice by",
                            "choosing",
                            room_choice, ":( YOU DIED!!!!")

                        elif choice4 == 'yes':
                            print('You have not reached the secret room, but',
                            'you reached the secret hallway.')
                            print('Would you like to enter it?')
                            print("Please enter either 'yes' or 'no'")
                            hallway_choice = str(raw_input('Type: '))
                            print("You made the right choice by choosing",
                            hallway_choice,". However, Nibodh is evil so you",
                            "died.")
                        else:
                            print("We don't understand gibberish, you died.")

                        # This is for the fireball choice
                    elif choice3 == 'dodge':
                        print('The fireball is too big for you, you should eat'
                        'it.')
                        print('Now you have to restart!')
                        print("Press the up arrow and then enter to restart")
                    else:
                        print("We don't understand gibberish, you died.")

                        # This is for the lava obstacle
                elif choice2 == 'jump':
                    print('Are you kidding me? Why would you think you would',
                    ' make it?')
                    print('You burned in lava')
                    print("Press the up arrow and then enter to restart")
                else:
                    print("We don't understand gibberish, you died.")

                        # This is for the goomba obstacles.
            elif choice1== 'yes':
                print("The goomba ate you")
                print("You died")
                print("Press the up arrow and then enter to restart")
            else:
                print("We don't understand gibberish, you died.")
        else:
            print("We don't understand gibberish, you died.")

    castle()

mario_game()