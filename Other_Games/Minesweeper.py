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

def minesweeper_game_5():
  print "This is a one player minesweeper game."
  print "Type in a row and column to try to find where the mine is."
  print "You are not typing in the mine's location, instead, type in"
  print "coordinates that you think are close to the mines."
  print "A _ means that you haven't guessed there yet."
  print "A 0 means that there are no mines within one unit."
  print "A 1 means that there are one mine within one unit."
  print "A 2 means that there are two mines within one unit."
  print "To flag where the mine is, type in -1 for row and -1 for column."
  print "Be sure to type in only NUMBERS from 1 through 5."
  print "Remember, row is HORIZONTAL and column is VERTICAL."
  print "Have Fun!!"

  board = []

  board.append([" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 "])

  for x in range(0, 5):
    board.append([str(x + 1), " _ ", " _ ", " _ ", " _ ", " _ "])
    #board.append([" _ "] * 5)

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_col(board):
    return randint(1, len(board[0]) - 1)

  def random_row(board):
    return randint(1, len(board) - 1)

  mine_row = random_row(board)
  mine_col = random_col(board)

  mine_row1 = random_row(board)
  mine_col1 = random_col(board)

  while mine_col1 == mine_col and mine_row1 == mine_row:
    if mine_col1 == mine_col:
      mine_col1 = random_col(board)
    elif mine_row1 == mine_row:
      mine_row1 = random_row(board)


  """
  print ""
  print "MINE LOCATIONS"
  print mine_row, mine_col
  print mine_row1, mine_col1
  """

  for turn in range(1, 20):
    print ""
    print ""
    print "Turn", turn

    guess_row = (int(raw_input("Guess Row: ")))
    guess_col = (int(raw_input("Guess Column: ")))

    if guess_row == mine_row and guess_col == mine_col or \
    guess_row == mine_row1 and guess_col == mine_col1:
      print "Oops, you hit a mine"
      break

    else:
      if guess_row not in range(6) or \
        guess_col not in range(6):

        if guess_col == -1 and guess_row == -1:
          print_board(board)
          print ""
          print("Do you know where a mine is? (yes/no)")
          answer = str(raw_input("Type: ")).lower()
          if answer == "yes":
            answer_mine_row = (int(raw_input("Guess Row:")))
            answer_mine_col = (int(raw_input("Guess Column:")))

            if answer_mine_row == mine_row and \
            answer_mine_col == mine_col or \
            answer_mine_row == mine_row1 and \
            answer_mine_col == mine_col1:
              print "Correct Answer"
              board[answer_mine_row][answer_mine_col] = " X "
            else:
              print "Incorrect"

        elif guess_col == -2 and guess_row == -2:
          print ""
          break

        else:
          print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == " X ":
        print( "You guessed that one already." )


      elif guess_row == 0 or guess_col == 0:
        print "Oops, that's not even in the ocean."

      else:

        board[guess_row][guess_col] = " 0 "

        def mine_location(row, row1, column, column1, count):
          if row - 1 == row1 \
            or row + 1 == row1 \
            or row == row1:
              if column == column1 or \
              column - 1 == column1 or \
              column + 1 == column1:
                if count == 1:
                  board[row][column] = " 1 "
                elif count == 2:
                  board[row][column] = " 2 "
          '''
          if board[guess_row][guess_col] == " 0 ":
            if row - 1 != row1 \
              or row   != row1 \
              or row != row1:
                if column != column1 or \
                column - 1 != column1 or \
                column   != column1:
                  board[row][column] = " 0 "
          '''
        count = 1

        mine_location(guess_row, mine_row, guess_col, mine_col, count)

        if board[guess_row][guess_col] == " 0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 ":
          count = 2

        mine_location(guess_row, mine_row1, guess_col, mine_col1, count)

      if board[mine_row][mine_col] == " X " and \
      board[mine_row1][mine_col1] == " X ":
        print ""
        print "Congragulations, you win in", turn, "turns."
        print_board(board)
        break

      if (turn == 50):
        print "Game Over"
        print "The first mine was at", mine_row, ",", mine_col
        print "The second mine was at", mine_row1, ",", mine_col1

      print_board(board)


def minesweeper_game_8():
  print "This is a one player minesweeper game."
  print "Type in a row and column to try to find where the mine is."
  print "You are not typing in the mine's location, instead, type in"
  print "coordinates that you think are close to the mines."
  print "A _ means that you haven't guessed there yet."
  print "A 0 means that there are no mines within one unit."
  print "A 1 means that there are one mine within one unit."
  print "A 2 means that there are two mines within one unit and so forth"
  print "To flag where the mine is, type in -1 for row and -1 for column."
  print "Be sure to type in only NUMBERS from 1 through 8."
  print "Remember, row is HORIZONTAL and column is VERTICAL."
  print "Have Fun!!"

  board = []

  board.append([" ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "])

  for x in range(0, 8):
    board.append([str(x + 1), " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "])
    #board.append([" _ "] * 8)

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_col(board):
    return randint(1, len(board[0]) - 1)

  def random_row(board):
    return randint(1, len(board) - 1)

  mine_row1 = random_row(board)
  mine_col1 = random_col(board)

  mine_row2 = random_row(board)
  mine_col2 = random_col(board)

  mine_row3 = random_row(board)
  mine_col3 = random_col(board)

  mine_row4 = random_row(board)
  mine_col4 = random_col(board)

  mine_row5 = random_row(board)
  mine_col5 = random_col(board)

  mine_row6 = random_row(board)
  mine_col6 = random_col(board)

  mine_row7 = random_row(board)
  mine_col7 = random_col(board)

  mine_row8 = random_row(board)
  mine_col8 = random_col(board)


  """
  print ""
  print "MINE LOCATIONS"
  print mine_row1, mine_col1
  print mine_row2, mine_col2
  print mine_row3, mine_col3
  print mine_row4, mine_col4
  print mine_row5, mine_col5
  print mine_row6, mine_col6
  print mine_row7, mine_co7
  print mine_row8, mine_col8
  """

  for turn in range(1, 80):
    print ""
    print ""
    print "Turn", turn

    guess_row = (int(raw_input("Guess Row: ")))
    guess_col = (int(raw_input("Guess Column: ")))

    if guess_row == mine_row1 and guess_col == mine_col1 or \
    guess_row == mine_row2 and guess_col == mine_col2 or \
    guess_row == mine_row3 and guess_col == mine_col3 or \
    guess_row == mine_row4 and guess_col == mine_col4 or \
    guess_row == mine_row5 and guess_col == mine_col5 or \
    guess_row == mine_row6 and guess_col == mine_col6 or \
    guess_row == mine_row7 and guess_col == mine_col7 or \
    guess_row == mine_row8 and guess_col == mine_col8:
      print "Oops, you hit a mine"
      break

    else:
      if guess_row not in range(9) or \
        guess_col not in range(9):

        if guess_col == -1 and guess_row == -1:
          print_board(board)
          print ""
          print("Do you know where a mine is? (yes/no)")
          answer = str(raw_input("Type: ")).lower()
          if answer == "yes":
            answer_mine_row = (int(raw_input("Guess Row:")))
            answer_mine_col = (int(raw_input("Guess Column:")))

            if answer_mine_row == mine_row1 and \
            answer_mine_col == mine_col1 or \
            answer_mine_row == mine_row2 and \
            answer_mine_col == mine_col2 or \
            answer_mine_row == mine_row3 and \
            answer_mine_col == mine_col3 or \
            answer_mine_row == mine_row4 and \
            answer_mine_col == mine_col4 or \
            answer_mine_row == mine_row5 and \
            answer_mine_col == mine_col5 or \
            answer_mine_row == mine_row6 and \
            answer_mine_col == mine_col6 or \
            answer_mine_row == mine_row7 and \
            answer_mine_col == mine_col7 or \
            answer_mine_row == mine_row8 and \
            answer_mine_col == mine_col8:
              print "Correct Answer"
              board[answer_mine_row][answer_mine_col] = " X "
            else:
              print "Incorrect"

        elif guess_col == -2 and guess_row == -2:
          print ""
          break

        else:
          print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == " X ":
        print( "You guessed that one already." )


      elif guess_row == 0 or guess_col == 0:
        print "Oops, that's not even in the ocean."

      else:

        board[guess_row][guess_col] = " 0 "

        def mine_location(row, row1, column, column1, count):
          if row - 1 == row1 \
            or row + 1 == row1 \
            or row == row1:
              if column == column1 or \
              column - 1 == column1 or \
              column + 1 == column1:
                if count == 1:
                  board[row][column] = " 1 "
                elif count == 2:
                  board[row][column] = " 2 "
                elif count == 3:
                  board[row][column] = " 3 "
                elif count == 4:
                  board[row][column] = " 4 "
                elif count == 5:
                  board[row][column] = " 5 "
                elif count == 6:
                  board[row][column] = " 6 "
                elif count == 7:
                  board[row][column] = " 7 "
                elif count == 8:
                  board[row][column] = " 8 "

        count = 1

        mine_location(guess_row, mine_row1, guess_col, mine_col1, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2

        mine_location(guess_row, mine_row2, guess_col, mine_col2, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3

        mine_location(guess_row, mine_row3, guess_col, mine_col3, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4

        mine_location(guess_row, mine_row4, guess_col, mine_col4, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5

        mine_location(guess_row, mine_row5, guess_col, mine_col5, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6

        mine_location(guess_row, mine_row6, guess_col, mine_col6, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7

        mine_location(guess_row, mine_row7, guess_col, mine_col7, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7
        elif board[guess_row][guess_col] == " 7 " or "  7 ":
          count = 8

        mine_location(guess_row, mine_row8, guess_col, mine_col8, count)


      if board[mine_row1][mine_col1] == " X " and \
      board[mine_row2][mine_col2] == " X " and \
      board[mine_row3][mine_col3] == " X " and \
      board[mine_row4][mine_col4] == " X " and \
      board[mine_row5][mine_col5] == " X " and \
      board[mine_row6][mine_col6] == " X " and \
      board[mine_row7][mine_col7] == " X " and \
      board[mine_row8][mine_col8] == " X ":
        print ""
        print "Congragulations, you win in", turn, "turns."
        print_board(board)
        break

      if (turn == 80):
        print "Game Over"
        print "The first mine was at", mine_row1, ",", mine_col1
        print "The second mine was at", mine_row2, ",", mine_col2
        print "The third mine was at", mine_row3, ",", mine_col3
        print "The fourth mine was at", mine_row4, ",", mine_col4
        print "The fifth mine was at", mine_row5, ",", mine_col5
        print "The sixth mine was at", mine_row6, ",", mine_col6
        print "The seventh mine was at", mine_row7, ",", mine_col7
        print "The eigth mine was at", mine_row8, ",", mine_col8

      print_board(board)



def minesweeper_game_10():
  print "This is a one player minesweeper game."
  print "Type in a row and column to try to find where the mine is."
  print "You are not typing in the mine's location, instead, type in"
  print "coordinates that you think are close to the mines."
  print "A _ means that you haven't guessed there yet."
  print "A 0 means that there are no mines within one unit."
  print "A 1 means that there are one mine within one unit."
  print "A 2 means that there are two mines within one unit and so forth"
  print "To flag where the mine is, type in -1 for row and -1 for column."
  print "Be sure to type in only NUMBERS from 1 through 8."
  print "Remember, row is HORIZONTAL and column is VERTICAL."
  print "Have Fun!!"

  board = []

  board.append(["  ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "])

  for x in range(0, 9):
    board.append([str(x + 1), "  _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "])
  board.append([str(10), " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "])

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  def random_col(board):
    return randint(1, len(board[0]) - 1)

  def random_row(board):
    return randint(1, len(board) - 1)

  mine_row10 = random_row(board)
  mine_col10 = random_col(board)

  mine_row1 = random_row(board)
  mine_col1 = random_col(board)

  mine_row2 = random_row(board)
  mine_col2 = random_col(board)

  mine_row3 = random_row(board)
  mine_col3 = random_col(board)

  mine_row4 = random_row(board)
  mine_col4 = random_col(board)

  mine_row5 = random_row(board)
  mine_col5 = random_col(board)

  mine_row6 = random_row(board)
  mine_col6 = random_col(board)

  mine_row7 = random_row(board)
  mine_col7 = random_col(board)

  mine_row8 = random_row(board)
  mine_col8 = random_col(board)

  mine_row9 = random_row(board)
  mine_col9 = random_col(board)


  """
  print ""
  print "MINE LOCATIONS"
  print mine_row1, mine_col1
  print mine_row2, mine_col2
  print mine_row3, mine_col3
  print mine_row4, mine_col4
  print mine_row5, mine_col5
  print mine_row6, mine_col6
  print mine_row7, mine_co7
  print mine_row8, mine_col8
  print mine_row9, mine_col9
  print mine_row10, mine_col0
  """

  for turn in range(1, 80):
    print ""
    print ""
    print "Turn", turn

    guess_row = (int(raw_input("Guess Row: ")))
    guess_col = (int(raw_input("Guess Column: ")))

    if guess_row == mine_row10 and guess_col == mine_col10 or \
    guess_row == mine_row1 and guess_col == mine_col1 or \
    guess_row == mine_row2 and guess_col == mine_col2 or \
    guess_row == mine_row3 and guess_col == mine_col3 or \
    guess_row == mine_row4 and guess_col == mine_col4 or \
    guess_row == mine_row5 and guess_col == mine_col5 or \
    guess_row == mine_row6 and guess_col == mine_col6 or \
    guess_row == mine_row7 and guess_col == mine_col7 or \
    guess_row == mine_row8 and guess_col == mine_col8 or \
    guess_row == mine_row9 and guess_col == mine_col9:
      print "Oops, you hit a mine"
      break

    else:
      if guess_row not in range(11) or \
        guess_col not in range(11):

        if guess_col == -1 and guess_row == -1:
          print_board(board)
          print ""
          print("Do you know where a mine is? (yes/no)")
          answer = str(raw_input("Type: ")).lower()
          if answer == "yes":
            answer_mine_row = (int(raw_input("Guess Row:")))
            answer_mine_col = (int(raw_input("Guess Column:")))

            if answer_mine_row == mine_row10 and \
            answer_mine_col == mine_col10 or \
            answer_mine_row == mine_row1 and \
            answer_mine_col == mine_col1 or \
            answer_mine_row == mine_row2 and \
            answer_mine_col == mine_col2 or \
            answer_mine_row == mine_row3 and \
            answer_mine_col == mine_col3 or \
            answer_mine_row == mine_row4 and \
            answer_mine_col == mine_col4 or \
            answer_mine_row == mine_row5 and \
            answer_mine_col == mine_col5 or \
            answer_mine_row == mine_row6 and \
            answer_mine_col == mine_col6 or \
            answer_mine_row == mine_row7 and \
            answer_mine_col == mine_col7 or \
            answer_mine_row == mine_row8 and \
            answer_mine_col == mine_col8 or \
            answer_mine_row == mine_row9 and \
            answer_mine_col == mine_col9:
              print "Correct Answer"
              board[answer_mine_row][answer_mine_col] = " X "
            else:
              print "Incorrect"

        elif guess_col == -2 and guess_row == -2:
          print ""
          break

        else:
          print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == " X ":
        print( "You guessed that one already." )


      elif guess_row == 0 or guess_col == 0:
        print "Oops, that's not even in the ocean."

      else:

        board[guess_row][guess_col] = " 0 "

        def mine_location(row, row1, column, column1, count):
          if row - 1 == row1 or \
            row + 1 == row1 or \
            row == row1:
              if column == column1 or \
              column - 1 == column1 or \
              column + 1 == column1:
                if count == 1:
                  board[row][column] = " 1 "
                  if column == 1:
                    board[row][column] = "  1 "
                elif count == 2:
                  board[row][column] = " 2 "
                  if column == 1:
                    board[row][column] = "  2 "
                elif count == 3:
                  board[row][column] = " 3 "
                  if column == 1:
                    board[row][column] = "  3 "
                elif count == 4:
                  board[row][column] = " 4 "
                  if column == 1:
                    board[row][column] = "  4 "
                elif count == 5:
                  board[row][column] = " 5 "
                  if column == 1:
                    board[row][column] = "  5 "
                elif count == 6:
                  board[row][column] = " 6 "
                  if column == 1:
                    board[row][column] = "  6 "
                elif count == 7:
                  board[row][column] = " 7 "
                  if column == 1:
                    board[row][column] = "  7 "
                elif count == 8:
                  board[row][column] = " 8 "
                  if column == 1:
                    board[row][column] = "  8 "
                elif count == 9:
                  board[row][column] = " 9 "
                  if column == 1:
                    board[row][column] = "  9 "
                elif count == 10:
                  board[row][column] = " 10 "
                  if column == 1:
                    board[row][column] = "  10 "

        count = 1

        mine_location(guess_row, mine_row1, guess_col, mine_col1, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2

        mine_location(guess_row, mine_row2, guess_col, mine_col2, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3

        mine_location(guess_row, mine_row3, guess_col, mine_col3, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4

        mine_location(guess_row, mine_row4, guess_col, mine_col4, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5

        mine_location(guess_row, mine_row5, guess_col, mine_col5, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6

        mine_location(guess_row, mine_row6, guess_col, mine_col6, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7

        mine_location(guess_row, mine_row7, guess_col, mine_col7, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7
        elif board[guess_row][guess_col] == " 7 " or "  7 ":
          count = 8

        mine_location(guess_row, mine_row8, guess_col, mine_col8, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7
        elif board[guess_row][guess_col] == " 7 " or "  7 ":
          count = 8
        elif board[guess_row][guess_col] == " 8 " or "  8 ":
          count = 9

        mine_location(guess_row, mine_row9, guess_col, mine_col9, count)

        if board[guess_row][guess_col] == " 0 " or "  0 ":
          count = 1
        elif board[guess_row][guess_col] == " 1 " or "  1 ":
          count = 2
        elif board[guess_row][guess_col] == " 2 " or "  2 ":
          count = 3
        elif board[guess_row][guess_col] == " 3 " or "  3 ":
          count = 4
        elif board[guess_row][guess_col] == " 4 " or "  4 ":
          count = 5
        elif board[guess_row][guess_col] == " 5 " or "  5 ":
          count = 6
        elif board[guess_row][guess_col] == " 6 " or "  6 ":
          count = 7
        elif board[guess_row][guess_col] == " 7 " or "  7 ":
          count = 8
        elif board[guess_row][guess_col] == " 8 " or "  8 ":
          count = 9
        elif board[guess_row][guess_col] == " 9 " or "  9 ":
          count = 10

        mine_location(guess_row, mine_row10, guess_col, mine_col10, count)

      if board[mine_row10][mine_col10] == " X " and \
      board[mine_row1][mine_col1] == " X " and \
      board[mine_row2][mine_col2] == " X " and \
      board[mine_row3][mine_col3] == " X " and \
      board[mine_row4][mine_col4] == " X " and \
      board[mine_row5][mine_col5] == " X " and \
      board[mine_row6][mine_col6] == " X " and \
      board[mine_row7][mine_col7] == " X " and \
      board[mine_row8][mine_col8] == " X " and \
      board[mine_row9][mine_col9] == " X ":
        print ""
        print "Congragulations, you win in", turn, "turns."
        print_board(board)
        break

      if (turn == 80):
        print "Game Over"
        print "The first mine was at", mine_row1, ",", mine_col1
        print "The second mine was at", mine_row2, ",", mine_col2
        print "The third mine was at", mine_row3, ",", mine_col3
        print "The fourth mine was at", mine_row4, ",", mine_col4
        print "The fifth mine was at", mine_row5, ",", mine_col5
        print "The sixth mine was at", mine_row6, ",", mine_col6
        print "The seventh mine was at", mine_row7, ",", mine_col7
        print "The eigth mine was at", mine_row8, ",", mine_col8
        print "The ninth mine was at", mine_row9, ",", mine_col9
        print "The tenth mine was at", mine_row10, ",", mine_col10

      print_board(board)



def replay():
    '''  This part of our game is  where we ask the user wehther or not they
    want to play again.  The user inputs either yes or no and depending on that
    the system will play the game again or end it.s
    '''

    print "Do you want to play this minesweeper game?"
    print "Type in 'yes' or 'no'."
    ans1 = str(raw_input('Type: \n')).lower()


    int1 = 1

    if ans1 == 'yes':
        int1 = 0
        print ""
        print"This game was created by Keenan Kalra. (2019)"
        print ""


    elif ans1 == 'no':
        print("Bye, have a good day!!")

    else:
      print "How hard is it to type in 'yes' or 'no'?"

    while int1 == 0:

      print "Do you want to play easy, medium, or hard version?"
      print "Type in either 'easy', 'medium', 'hard'."
      ans2 = str(raw_input('Type: \n')).lower()

      if ans2 == 'easy':
        print ""
        print ""
        print ""
        minesweeper_game_5()
      elif ans2 == 'medium':
        print ""
        print ""
        print ""
        minesweeper_game_8()
      elif ans2 == 'hard':
        print ""
        print ""
        print ""
        minesweeper_game_10()
      else:
        print "How hard is it to type in 'easy' or 'medium' or 'hard'?"
        break

      print ""
      print "Do you want to play again?"
      print "Type in 'yes' or 'no'."
      ans1 = str(raw_input('Type: \n')).lower()

      int1 = 1

      if ans1 == 'yes':
          print ""
          int1 = 0
      elif ans1 == 'no':
          print "Bye, have a good day!!"
      else:
          print "We didn't understand you so you can't play again."
          print "If you want to play, press the up arrow and then enter."

replay()
