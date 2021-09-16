#Initial data
import os
import json
import time
raw = os.popen("termux-volume").read()
value = json.loads(raw)
previous = value[3]['volume']

#Manage volume
while True:

  #Get recent
  raw = os.popen("termux-volume").read()
  value = json.loads(raw)
  sound = value[3]['volume']

  #Decide if needed
  if sound < previous:
    os.system("termux-volume music 0")
    print("block, "+str(sound))
    time.sleep(28)
    os.system("termux-volume music "+str(previous))
    print("restore, "+str(previous))
