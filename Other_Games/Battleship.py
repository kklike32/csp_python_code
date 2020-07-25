from random import randint

print ""
print ""
print "  _  __                             _  __     _             ____   ___  _  ___"
print " | |/ /___  ___ _ __   __ _ _ __   | |/ /__ _| |_ __ __ _  |___ \ / _ \/ |/ _ \ "
print " | ' // _ \/ _ \ '_ \ / _` | '_ \  | ' // _` | | '__/ _` |   __) | | | | | (_) |"
print " | . \  __/  __/ | | | (_| | | | | | . \ (_| | | | | (_| |  / __/| |_| | |\__, |"
print " |_|\_\___|\___|_| |_|\__,_|_| |_| |_|\_\__,_|_|_|  \__,_| |_____|\___/|_|  /_/ "

print ""
print ""

def two_player():
  print "This is a two player battleship game."
  print "Each person will try to guess where the battleship is by typing in an"
  print "integer from 0 to 4 for guessing the row and column."
  print "After each turn, the board will show. The X represents where someone"
  "already guessed. Each person will get four turns to guess."
  print "Be sure to type in only numbers from 1 through 5."
  print "Have Fun!!"

  board = []

  for x in range(0, 5):
    board.append([" O "] * 5)

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  def random_row(board):
    return randint(0, len(board) - 1)

  ship_row = random_row(board)
  ship_col = random_col(board)

  # Everything from here on should be in your for loop
  # don't forget to properly indent!
  for turn in range(8):
    print "Turn", turn + 1

    player = 'A'

    if turn % 2 == 0:
      print "Player A turn"
    else:
      print "Player B turn"
      player = 'B'

    guess_row = (int(raw_input("Guess Row: "))) - 1
    guess_col = (int(raw_input("Guess Column: "))) - 1

    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! Player", player, "sank my", "battleship!"
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == " X ":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = " X "
      if (turn == 8):
        print "Game Over"
        print "The row was", ship_row
        print "The column was", ship_col
      print_board(board)


def one_player():
  print "This is a one player battleship game."
  print "You will try to guess where the battleship is by typing in an"
  print "integer from 0 to 4 for guessing the row and column."
  print "After each turn, the board will show. The X represents where someone"
  "already guessed. You will get eight turns to guess."
  print "Be sure to type in only numbers from 1 through 5."
  print "Have Fun!!"

  board = []

  for x in range(0, 5):
    board.append([" O "] * 5)

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  def random_row(board):
    return randint(0, len(board) - 1)

  ship_row = random_row(board)
  ship_col = random_col(board)

  # Everything from here on should be in your for loop
  # don't forget to properly indent!
  for turn in range(8):
    print "Turn", turn + 1

    guess_row = (int(raw_input("Guess Row: "))) - 1
    guess_col = (int(raw_input("Guess Column: "))) - 1

    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! Player you sank my battleship!"
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == " X ":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = " X "
      if (turn == 8):
        print "Game Over"
        print "The row was", ship_row
        print "The column was", ship_col
      print_board(board)

def replay():
    '''  This part of our game is  where we ask the user whether or not they
    want to play again.  The user inputs either yes or no and depending on that
    the system will play the game again or end it.
    '''

    print"Do you want to play this battleship game?"
    print "Type in 'yes' or 'no'."
    ans1 = str(raw_input('Type: \n')).lower()


    int1 = 1

    if ans1 == 'yes':
        int1 = 0
        print ""
        print"This game was created by Keenan Kalra. (2019)"
        print ""

    elif ans1 == 'no':
        print"Bye, have a good day!!"

    else:
      print "How hard is it to type in 'yes' or 'no'?"

    while int1 == 0:

        print "How many people are playing? (1/2)"
        ans2 = str(raw_input("Type: \n")).lower()
        if ans2 == "1":
          one_player()
        elif ans2 == "2":
          two_player()

        else:
          print"We didn't understand you so you can't play."
          print"If you want to play, press the up arrow and then enter."
          break

        print ""
        print"Do you want to play again?"
        print"Type in 'yes' or 'no'."
        ans1 = str(raw_input('Type: \n')).lower()

        int1 = 1

        if ans1 == 'yes':
            print ""
            int1 = 0
        elif ans1 == 'no':
            print"Bye, have a good day!!"
        else:
            print"We didn't understand you so you can't play again."
            print"If you want to play, press the up arrow and then enter."
            break

replay()