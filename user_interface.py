import sys
import os
import time
import subprocess
from sniff_search import sniffPref
from menu import menu

def userInterface():
  #clears CLI 
  platform = sys.platform
  if platform == 'win32':
    subprocess.call('CLS', shell=True)
  else:
    subprocess.call('clear', shell=True)

  # ascII art :)
  print("###################################################################")
  print("###################################################################")
  print("\n")
  print("                    _   __   __         _                   ")
  print("        ___  _ __  (_) / _| / _| _   _ | |__    ___   _   _ ")
  print("       / __|| '_ \ | || |_ | |_ | | | || '_ \  / _ \ | | | |")
  print("       \__ \| | | || ||  _||  _|| |_| || |_) || (_) || |_| |")
  print("       |___/|_| |_||_||_|  |_|   \__, ||_.__/  \___/  \__, |")
  print("                                 |___/                |___/ ") 
  print("") 
  print("                   \/----\/")
  print("                    \ 0 0/    WOOF! WHO AM I NETWORKING WITH?!")
  print("                    _\  /_")
  print("                  _|  \/  |_")
  print("                 | | |  | | | ")
  print("                _| | |  | | |_")
  print("                ---|_|--|_|---")
  print("\n")
  print("###################################################################")
  print("###################################################################")

  menu()


if __name__ == "__main__":
  userInterface()