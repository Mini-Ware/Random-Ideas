import random
progress = True
result = ""
choice = ""

#2d array
board = [["  ","  ","  "],
         ["  ","  ","  "],
         ["  ","  ","  "]]

#Functions
def check(progress, board):

  #Game over
  loopx = 0
  loopy = 0

  #Check horizontal
  while loopy < 3:
    if board[loopy][0] == "X " and board[loopy][1] == "X " and board[loopy][2] == "X ":
      result = "win"
      progress = False
    elif board[loopy][0] == "O " and board[loopy][1] == "O " and board[loopy][2] == "O ":
      result = "lose"
      progress = False
    loopy = loopy + 1

  #Check vertical
  while loopx < 3:
    if board[0][loopx] == "X " and board[1][loopx] == "X " and board[2][loopx] == "X ":
      result = "win"
      progress = False
    elif board[0][loopx] == "O " and board[1][loopx] == "O " and board[2][loopx] == "O ":
      result = "lose"
      progress = False
    loopx = loopx + 1

  #Check diagonal
  if board[0][0] == "X " and board[1][1] == "X " and board[2][2] == "X ":
    result = "win"
    progress = False
  elif board[0][0] == "O " and board[1][1] == "O " and board[2][2] == "O ":
    result = "lose"
    progress = False
  elif board[0][2] == "X " and board[1][1] == "X " and board[2][0] == "X ":
    result = "win"
    progress = False
  elif board[0][2] == "O " and board[1][1] == "O " and board[2][0] == "O ":
    result = "lose"
    progress = False

  #Check draw
  if board[0][0] != "  " and board[0][1] != "  " and board[0][2] != "  " and board[1][0] != "  " and board[1][1] != "  " and board[1][2] != "  " and board[2][0] != "  " and board[2][1] != "  " and board[2][2] != "  ":
    result = "draw"
    progress = False

  if progress == False:
    if result == "win":
      print("You won!")
    elif result == "lose":
      print("You lost!")
    elif result == "draw":
      print("Its a draw!")
  return progress

#Main loop
while progress:
  confirm = False
  position = int(input("Select a square (1-9): "))-1
  x = 0
  y = 0

  #Update board
  if position > 5:
    x = position - 6
    y = 2
  elif position > 2:
    x = position - 3
    y = 1
  else:
    x = position
    y = 0

  if board[y][x] == "  ":
    board[y][x] = "X "
  else:
    print("That square has already been occupied!")
    confirm = True
  check(progress, board)

  #Response
  loopx = 0
  loopy = 0
  move = 0

  #Block horizontal

  #Block vertical

  #Block diagonal

  #Anyhow place
  while confirm == False:
    move = random.randint(0,8)
    if move > 5:
      x = move - 6
      y = 2
    elif move > 2:
      x = move - 3
      y = 1
    else:
      x = move
      y = 0

    if board[y][x] == "  ":
      board[y][x] = "O "
      confirm = True

  check(progress, board)
  print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")
