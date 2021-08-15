import random
progress = True
choice = ""

#2d array
board = [["  ","  ","  "],
         ["  ","  ","  "],
         ["  ","  ","  "]]

#Main loop
while progress:
  choice = int(input("Select a square (1-9): "))-1

  #Update board
  if choice > 5:
    choice = choice - 6
    board[2][choice] = "X "
  elif choice > 2:
    choice = choice - 3
    board[1][choice] = "X "
  else:
    board[0][choice] = "X "

  #Response
  print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")

  #Game over
  if :
    print("You won!")
  elif :
    print("You lost!")
