import random
progress = True
result = ""
choice = ""

#2d array
board = [["  ","  ","  "],
         ["  ","  ","  "],
         ["  ","  ","  "]]

#Main loop
while progress:
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

  #Response
  print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")

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
    if result == "win":
      print("You won!")
    elif result == "lose":
      print("You lost!")
