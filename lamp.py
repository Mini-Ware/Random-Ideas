#Default settings
import os
import json
import time
switch = 0

#Check brightness
while True:

  #Retrive intensity
  raw = os.popen("termux-sensor -s light -n 1 -d 10").read()
  value = json.loads(raw)
  intensity = value['LIGHT']['values'][0]

  #Decide if light is needed
  if intensity <= 8 and switch == 0:
    switch = 1
    print("on, "+str(intensity))
    os.system("termux-torch on")
  if intensity > 8 and switch == 1:
    switch = 0
    print("off, "+str(intensity))
    os.system("termux-torch off")
