from __future__ import print_function
import random

'''  This theme of our hangman were based upon our two interests, basketball
and football.  The game first opens with the player being able to choose whether
they want to do NBA teams, or NFL teams.  After they choose that, they are given
the whole word and how many letter the word is.  The user inputs a letter and
the computer inputs whether or not that the program is in the game.
'''

def hangman():
    '''This part of game contains all of the teams (secrets) which the user
    user will have to guess.  The input which the player puts is whether they
    want the NFL version of our game or the NBA version of our game.  The progr
    am then puts the secret word letters.
    '''

    # This is all 30 nba teams which the player can choose.
    nba_teams = [
    "WARRIORS", "LAKERS", "HAWKS", "CELTICS", "NETS", "HORNETS", "BULLS",
    "CAVALIERS", "MAVERICKS", "NUGGETS", "PISTONS", "ROCKETS", "PACERS",
    "CLIPPERS", "GRIZZLIES", "HEAT", "BUCKS", "TIMBERWOLVES", "PELICANS",
    "KNICKS", "THUNDER", "MAGIC", "SUNS", "BLAZERS", "KINGS", "SPURS",
    "RAPTORS", "JAZZ", "SIXERS", "WIZARDS"
    ]


    # These are all the teams which the user may have if they choose NFL
    nfl_teams = ['BRONCOS', 'LIONS', 'PACKERS', 'TEXANS', 'COLTS', 'JAGUARS',
    'CHIEFS', 'DOLPHINS', 'VIKINGS', 'PATRIOTS', 'SAINTS', 'GIANTS', 'JETS',
    'RAIDERS', 'EAGLES', 'STEELERS', 'CHARGERS', 'SEAHAWKS', 'RAMS',
    'BUCCANERS', 'TITANS', 'REDSKINS', 'CARDINALS', 'COWBOYS', 'BROWNS',
    'BENGALS', 'BEARS', 'PANTHERS', 'BILLS', 'RAVENS', 'FALCONS']

    guessed_letters = []

    print()
    print("Do you want to play single player or two player version?")
    print("Type in 'single' or 'double'.")
    game_choice = str(input())

    if game_choice == "double":
        print("Welcome, two players. Choose who is player one")
        print("who is player number 2")
        print()
        print("Player number one, please type in a secret.")
        print("It has to be a single word!!!")
        game_choice1 = str(input())
        secret = game_choice1
        print("Okay, the secret is '", secret, "' .")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

    elif game_choice == "single":
        print("Welcome, one player.")

        # Chooses a random team from the NFL list.
        secret = random.choice(nfl_teams)

        # Asking the user which game mode they want.
        print()
        print("Do you want NFL teams or NBA teams as your theme for this game?")
        print()
        print("Type in 'NFL' or 'NBA'.")

        choice = str(input('Type: \n')).upper()

        if choice == 'NBA':
            secret = random.choice(nba_teams)
            print("NBA time")
        else:
            secret = random.choice(nfl_teams)
            print("NFL time")

    else:
        print("Sorry, we could not understand you. ")

    guess_word = []
    length_word = len(secret)

    #  We use /n to print the commands on different lines.
    def intro():
        '''  This function in our game has no inputs that are required by the
        user, but it has what the program will print to the terminal.  All this
        function is used for is basic instructions on how our game works.
        '''
        print()
        print("Welcome to our hangman game!! \n")
        print()
        if game_choice == "single":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("             TURN ON CAPS LOCK RIGHT NOW!!!!! \n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
        print("To play, type in a LETTER that you think is in the secret.")
        print()
        print("If you think you know the secret, type in the secret.")
        print()
        print("If you type in more than one letter(and it's not the secret),you"
              , "will lose a turn.")
        print()
        print("You have", length_word, "tries to try to guess the secret.")
        print("Good Luck!!")



    def dis_guess():
        '''  This function is used for the start of our game where it takes the
        secret word and converts it into the parenthesis.  There are no inputs
        which the user has to put here beside just reading the instructions.  It
        also tells how many characters the word is.
        '''
        for char in secret:
            guess_word.append(" _ ")
        print(*guess_word, sep=' ')
        print ()
        print("The secret word is", length_word, "letters long. \n")

    def tell_secret():
        '''For the purpose of grading and gallery walk we made a feature which
        had the secret word already placed there to make it easier for game play
        to be easier.
        '''

        print("Do you want to know the secret now?")
        print("Type in 'yes' or 'no'.")

        # Converts all word word into lowercase to make it easier
        ans = str(input('Type: \n')).lower()
        if ans == 'yes':
            print()
            print("The secret is", secret)
        elif ans == "no":
            print()
            print("Alright, continue to the game.")

    def hangman_game():
        '''  This function is the main part of our game and contains the
        dis_guess and intro function which we will use when we initiate the
        game. There is no need to input this function into the terminal as we
        already have it running.
        '''
        intro()

        dis_guess()

        tell_secret()

        count = length_word

        #  This variable is called later at the bottom, used for the hangman
        #characters.
        turns = 10

        # Count is used for the letters guessed so we can tell the player which
        #letters they have used.
        while count > 0:

            print ()
            print("You have guessed the following letters...")
            print (*guessed_letters, sep = ", ")
            print ()

            guess = input("Type a character or the entire secret: \n")

            # Adds the correctly guessed letters into the to actual word

            guessed_letters.append(guess)

            if guess in secret:

                if guess == "":
                    print ()
                    print("Oops, type in a letter.")

                elif len(guess) > 1:
                    if guess == secret:
                        print()
                        print(secret)
                        print ()
                        print("Congrats, you won with", count - 1, "turn(s)",
                        "left.")
                        break
                    else:
                        print ()
                        print("Oops, type in ONE letter or the entire secret",
                        "phrase. \n")
                else:
                    print()
                    print("Good Job!! That's the correct letter. \n")

                    for i in range(0, length_word):
                        if secret[i] == guess:
                            guess_word[i] = guess

                    if " _ " not in guess_word:
                        print()
                        print(*guess_word, sep=' ')
                        print ()
                        print("Congrats, you won with", count -1, "turn(s)",
                        "left.")
                        break

            print()

            if guess not in secret:
                if turns == 10:
                    print()
                    print (" o")
                if turns == 9:
                    print ("\n")
                    print (" o")
                    print (" |")
                if turns == 8:
                    print ("\n")
                    print (" o \n"
                           " | \n"
                           "/")
                if turns == 7:
                    print ("\n")
                    print (" o \n"
                           " | \n"
                          "/ \ ")
                if turns == 6:
                    print ("\n")
                    print (" o \n"
                           " |- \n"
                          "/ \ ")
                if turns == 5:
                    print ("\n")
                    print (" o \n"
                          "-|- \n"
                          "/ \ ")
                if turns == 4:
                    print ("\n")
                    print ("  o \n"
                          " -|- \n"
                         "_/ \ ")
                if turns == 3:
                    print ("\n")
                    print ("  o \n"
                          " -|- \n"
                         "_/ \_")
                if turns == 2:
                    print ("\n")
                    print ("  o \n"
                          " /|- \n"
                         "_/ \_")
                if turns == 1:
                    print ("\n")
                    print ("  o \n"
                          " /|\ \n"
                         "_/ \_")
                turns -= 1

            print()
            print(*guess_word, sep=' ')

            count -= 1

            if count == 0:
                print()
                print("You ran out of turns!")
                print()
                print("The secret phrase was", secret)
            else:
                print ()
                print("You have", count, "turn(s) left.")
        print ()
        print ()
        print("Game Over")


    hangman_game()

def replay():
    '''  This part of our game is  where we ask the user wehther or not they
    want to play again.  The user inputs either yes or no and depending on that
    the system will play the game again or end it.
    '''

    print("Do you want to play this hangman game?")
    print("Type in 'yes' or 'no'.")
    ans1 = str(input('Type: \n')).lower()


    int1 = 1

    if ans1 == 'yes':
        int1 = 0
        print()
        print("This game was created by")
        print("    Keenan Kalra ")
        print("         &")
        print("Nibodh Vallapureddy")

    elif ans1 == 'no':
        print("Bye, have a good day!!")

    while int1 == 0:
        hangman()
        print("Do you want to play again?")
        print("Type in 'yes' or 'no'.")
        ans1 = str(input('Type: \n')).lower()

        int1 = 1

        if ans1 == 'yes':
            int1 = 0
        elif ans1 == 'no':
            print("Bye, have a good day!!")
        else:
            print("We didn't understand you so you can't play again")
            print("If you want to play, press the up arrow and then enter.")

replay()