import time
import random
import os
map = []
size = []
height = 0
width = 0

def reset():
  #Hide cursor
  os.system("tput civis")

  #Find screen area
  size = os.popen("stty size").read().split(" ")
  global height
  global width
  height = int(size[0])-1
  width = int(size[1])

  #Setup array map
  global map
  map = []
  i = 0
  while i < height:
    map.append([])
    n = 0
    while n < width:
      map[i].append(" ")
      n = n + 1
    i = i + 1                               
  return map

def fill(x1, x2, y1, y2, char):
  pass

def plot(x, y, char):
  map[y][x] = char

def draw():
  draft = ""
  i = 0
  while i < height:
    n = 0
    while n < width:
      draft = draft+map[i][n]
      n = n + 1
    draft = draft+"\n"
    i = i + 1
  print(draft, end="")

try:
  while True:
    reset()
    n = 0
    while n < 50:
      random_x = random.randint(0, width-1)
      random_y = random.randint(1, height-1)
      plot(random_x, random_y, "*")
      n = n + 1
    draw()
    time.sleep(1)
except:
  os.system("tput cnorm")
