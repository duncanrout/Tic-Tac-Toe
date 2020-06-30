board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#variables
currentPlayer = "X"
gameRunning = True
winner = None

def play_game():
  display_board()
  
  while gameRunning:
    take_turn(currentPlayer)
    check_if_game_over()
    next_turn()
  if(winner == "X" or winner == "Y"):
    print(winner + " won!")
  else:
    print("Tie.")

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

def take_turn(player):
  print("player " + player + " take your turn!")
  index = input("Where would you like to go!?")

  valid = False
  while not valid:
    index = int(index) - 1
    if(board[index] == "-"):
      valid = True
    else:
      print("Invalid spot... Pick another!")

  board[index] = player
  display_board()

def next_turn():
  global currentPlayer
  if(currentPlayer == "X"):
    currentPlayer = "Y"
  else:
    currentPlayer = "X"
    
def check_if_game_over():
  check_for_tie()
  check_for_win()

def check_for_tie():
  global gameRunning

  if "-" not in board:
    gameRunning = False
    return True
  else:
    return False

def check_for_win():
  global gameRunning
  global winner
  
  # Check each row
  r1 = board[0] == board[1] == board[2] != "-"
  r2 = board[3] == board[4] == board[5] != "-"
  r3 = board[6] == board[7] == board[8] != "-"
  # Check each column
  c1 = board[0] == board[3] == board[6] != "-"
  c2 = board[1] == board[4] == board[7] != "-"
  c3 = board[2] == board[5] == board[8] != "-"
  # Check each diagonal
  d1 = board[0] == board[4] == board[8] != "-"
  d2 = board[2] == board[4] == board[6] != "-"
  
  # if any win conditions met, return who won
  if r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2:
    gameRunning = False
    if r1:
      winner = board[0] 
      return board[0] 
    elif r2:
      winner = board[3] 
      return board[3] 
    elif r3:
      winner = board[6] 
      return board[6]
    elif c1:
      winner = board[0] 
      return board[0] 
    elif c2:
      winner = board[1] 
      return board[1] 
    elif c3:
      winner = board[2] 
      return board[2]
    elif d1:
      winner = board[0] 
      return board[0] 
    elif d2:
      winner = board[2] 
      return board[2]
    else:
      return None

def check_for_tie():
  global gameRunning
  if "-" not in board:
    gameRunning = False
    return True
  else:
    return False
  
#Game Start
play_game()
  
    
  
  



    
    

