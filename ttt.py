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
  print(str(choice))

  #Response
  print(" —— —— ——\n|"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|\n —— —— ——\n|"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|\n —— —— ——\n|"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|\n —— —— ——")

  #Conditions
