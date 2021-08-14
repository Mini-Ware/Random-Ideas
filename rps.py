import random
import time
active = True
choice = ""
outcome1 = 0
oitcome2 = 0
option = ["Rock","Paper","Scissors"]

#Main loop
while active:
  outcome1 = random.randint(0,2)
  outcome2 = random.randint(0,2)
  print("Computer1: "+option[outcome1]+"\nComputer2: "+option[outcome2])

  #Determine outcome
  if outcome1 == outcome2:
    print("Winner: None")
  elif ((outcome1 == 1 and outcome2 == 0) or (outcome1 == 0 and outcome2 == 2) or (outcome1 == 2 and outcome2 == 1)):
    print("Winner: Computer1")
  else:
    print("Winner: Computer2")

  #Add delay
  time.sleep(1)
