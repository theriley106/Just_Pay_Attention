import os

os.system('mkfifo t cat t | omxplayer --no-osd -b video.mp4 &')

def play_pause():
  os.system('echo p > t rm t')