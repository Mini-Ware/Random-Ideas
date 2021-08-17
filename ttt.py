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

  if progress == False:
    print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")
    if result == "win":
      print("You won!")
      exit()
    elif result == "lose":
      print("You lost!")
      exit()

  return progress

def valid(progress, board):

  #Check draw
  if progress == True and board[0][0] != "  " and board[0][1] != "  " and board[0][2] != "  " and board[1][0] != "  " and board[1][1] != "  " and board[1][2] != "  " and board[2][0] != "  " and board[2][1] != "  " and board[2][2] != "  ":
    result = "draw"
    progress = False

  if progress == False:
    print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")
    if result == "draw":
      print("Its a draw!")
      exit()
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
  valid(progress, board)

  #Response
  loopx = 0
  loopy = 0
  move = 0

  #Solve horizontal
  while loopy < 3:
    if confirm == False and board[loopy][0] == "  " and board[loopy][1] == "O " and board[loopy][2] == "O ":
      board[loopy][0] = "O "
      confirm = True
    elif confirm == False and board[loopy][1] == "  " and board[loopy][0] == "O " and board[loopy][2] == "O ":
      board[loopy][1] = "O "
      confirm = True
    elif confirm == False and board[loopy][2] == "  " and board[loopy][0] == "O " and board[loopy][1] == "O ":
      board[loopy][2] = "O "
      confirm = True
    loopy = loopy + 1

  #Solve vertical
  while loopx < 3:
    if confirm == False and board[0][loopx] == "  " and board[1][loopx] == "O " and board[2][loopx] == "O ":
      board[0][loopx] = "O "
      confirm = True
    elif confirm == False and board[1][loopx] == "  " and board[0][loopx] == "O " and board[2][loopx] == "O ":
      board[1][loopx] = "O "
      confirm = True
    elif confirm == False and board[2][loopx] == "  " and board[0][loopx] == "O " and board[1][loopx] == "O ":
      board[2][loopx] = "O "
      confirm = True
    loopx = loopx + 1

  #Solve diagonal

  #Reset loops
  loopx = 0
  loopy = 0

  #Block horizontal
  while loopy < 3:
    if confirm == False and board[loopy][0] == "  " and board[loopy][1] == "X " and board[loopy][2] == "X ":
      board[loopy][0] = "O "
      confirm = True
    elif confirm == False and board[loopy][1] == "  " and board[loopy][0] == "X " and board[loopy][2] == "X ":
      board[loopy][1] = "O "
      confirm = True
    elif confirm == False and board[loopy][2] == "  " and board[loopy][0] == "X " and board[loopy][1] == "X ":
      board[loopy][2] = "O "
      confirm = True
    loopy = loopy + 1

  #Block vertical
  while loopx < 3:
    if confirm == False and board[0][loopx] == "  " and board[1][loopx] == "X " and board[2][loopx] == "X ":
      board[0][loopx] = "O "
      confirm = True
    elif confirm == False and board[1][loopx] == "  " and board[0][loopx] == "X " and board[2][loopx] == "X ":
      board[1][loopx] = "O "
      confirm = True
    elif confirm == False and board[2][loopx] == "  " and board[0][loopx] == "X " and board[1][loopx] == "X ":
      board[2][loopx] = "O "
      confirm = True
    loopx = loopx + 1

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
  valid(progress, board)
  print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")
