import sys
import os
import time
import subprocess
from testing import packetSniff
from logs import createTrafficLog

def userInterface():
  #clears CLI 
  platform = sys.platform
  if platform == 'win32':
    subprocess.call('CLS', shell=True)
  else:
    subprocess.call('clear', shell=True)

  # ascII art :)
  print("#########################################################")
  print("#########################################################")
  print("\n")
  print("                 _   __   __         _                   ")
  print("     ___  _ __  (_) / _| / _| _   _ | |__    ___   _   _ ")
  print("    / __|| '_ \ | || |_ | |_ | | | || '_ \  / _ \ | | | |")
  print("    \__ \| | | || ||  _||  _|| |_| || |_) || (_) || |_| |")
  print("    |___/|_| |_||_||_|  |_|   \__, ||_.__/  \___/  \__, |")
  print("                              |___/                |___/ ") 
  print("") 
  print("                \/----\/")
  print("                 \ 0 0/    WOOF! WHO AM I NETWORKING WITH?!")
  print("                 _\  /_")
  print("               _|  \/  |_")
  print("              | | |  | | | ")
  print("             _| | |  | | |_")
  print("             ---|_|--|_|---")
  print("\n")
  print("#########################################################")
  print("#########################################################")
  print("\n\n")

  # asks for user's length of operation, runs the sniffer for that amount of time, and creates a list of logs
  answer = int(input('How many seconds do you want to run SniffyBoy for?: '))
  timer_end = time.time() + answer
  pkts=[]
  while time.time() < timer_end:
    pkts.append(packetSniff())
  
  print('\nIntercepted {} packets within a {} second search!'.format(len(pkts), answer))
  
  # creates the actual log excel file from the stored logs [note: this function replaces the current standing log file]
  print('\nCreating log...\n')
  for x in range(5):
    print('.')
    time.sleep(1)
  
  createTrafficLog(pkts)
  print('\nCompleted log!\n')

  # notifies user of location of log file location and allows them to access it immediately after scan
  current = str(os.getcwd())
  
  print('You can find your log file at ' + current + '\logs.xlsx' +'\n\n')
  openfile = input('Would you like to access the file now (Y/N)?: ')
  if openfile == 'Y' or openfile == 'y':
    os.system("start " + current + '\logs.xlsx')
  elif openfile == 'N' or openfile == 'n':
    print('Thank you for using SniffyBoy!')
    sys.exit()
  else:
    print('That is an invalid command. For your protection, we are closing the program and clearing the log')
    os.remove('logs.xslx')




if __name__ == "__main__":
  userInterface()