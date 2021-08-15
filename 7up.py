current = 15
next = 0
alive = True

#Start counting
while alive:
  print("Current number: "+str(current))
  next = input("Next number: ")

  #Confirm if its a multiple
  if (current + 1) % 7 == 0:
    #Up should be next
    if next.lower() != "up":
      alive = False
      print("Your reply should be \"up\"!")

  #Find out if number contains 7
  elif str(current+1).find("7") != -1:
    #Up should be next
    if next.lower() != "up":
      alive = False
      print("Your reply should be \"up\"!")

  else:
    #Make sure its correct
    next = int(next)
    if next != current+1:
      alive = False
      print("Your reply should be "+str(current+1)+"!")

  #Update progress
  current = current+1
