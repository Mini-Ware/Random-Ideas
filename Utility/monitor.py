import requests
import time
import os

count = 0

while True:
  target = os.environ['TARGET']
  x = requests.get(target)
  result = x.text
  
  breaking = result.split("numVideosText")
  breaker = breaking[1].split('"')
  narrow = breaker[6]

  current = int(narrow)
  if count != 0 and count != current:
    print("Updated playlist!\nCurrent videos: "+narrow)
  
  count = current
  print(count)
  
  time.sleep(300)
