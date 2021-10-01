import speech_recognition as sr
import time
import os
from os import path
power = False
cmd = ""


#Configuration
SPEECH_FILE = "voice.mp3"
AUDIO_FILE = "voice.wav"

def say(text):
  os.system("termux-tts-speak "+text)

def do(task, current):
  print("User said: "+task)
  if task == "okay":
    say("okay")
  elif task == "flashlight":
    if current == False:
      say("turning on flashlight")
      os.system("termux-torch on")
    elif current == True:
      say("turning off flashlight")
      os.system("termux-torch off")
  elif task == "vibrate":
      say("vibrating phone")
      os.system("termux-vibrate")
  return power

#Capture audio
while True:

  #Begin
  input("Start?")
  os.system("termux-microphone-record -b 512 -l 0 -f voice.mp3")

  #Finish
  input("Stop?")
  os.system("termux-microphone-record -q")
  time.sleep(5)

  #Convert mp3 file to wav
  os.system("ffmpeg -i "+SPEECH_FILE+" "+AUDIO_FILE)
  os.system("rm "+SPEECH_FILE)

  #Transcribe audio file
  r = sr.Recognizer()

  #Use the audio file as the audio source
  with sr.AudioFile(AUDIO_FILE) as source:

      #Read the entire audio file
      audio = r.record(source)
      try:
        cmd = r.recognize_google(audio, language = "en-GB")
      except:
        cmd = ""
      do(cmd, power)
      os.system("rm "+AUDIO_FILE)
