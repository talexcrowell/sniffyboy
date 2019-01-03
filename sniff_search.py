import sys
import os
import time
import socket
import subprocess
from packet_sniffer import packetSniff
from logs import createTrafficLog
# from user_interface import userInterface

def sniffPref():
  #clears CLI 
  platform = sys.platform
  if platform == 'win32':
    subprocess.call('CLS', shell=True)
  else:
    subprocess.call('clear', shell=True)

  #system host check and preference setting
  hostName = socket.gethostname()
  HOST = socket.gethostbyname(socket.gethostname())
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
  print("                    \ 0 0/    WHEW! PACKETS CAN BE STINKY!")
  print("                    _\  /_")
  print("                  _|  \/  |_")
  print("                 | | |  | | | ")
  print("                _| | |  | | |_")
  print("                ---|_|--|_|---")
  print("\n")
  print("###################################################################")
  print("###################################################################")
  print("\n")
  print('\t\tYour HOST is {} (IP: {})\n\n'.format(hostName, HOST))
  print("###################################################################")
  print("###################################################################")
  print('\n')

  hostCheck = input('Would you like to log [A]ll, [I]ncoming, or [O]utgoing packets?: ')
  print('\n') 
  # asks for user's length of operation, runs the sniffer for that amount of time, and creates a list of logs
  answer = int(input('How many seconds do you want to run SniffyBoy for?: '))
  print('\nIntializing...\n')
  timer_end = time.time() + answer
  pkts=[]

  if hostCheck == 'A' or hostCheck == 'a':  
    while time.time() < timer_end:
      pkts.append(packetSniff())
  elif hostCheck == 'I' or hostCheck == 'i':
    while time.time() < timer_end:
      incomingPkt = packetSniff()
      if incomingPkt[1] != HOST:
        pkts.append(incomingPkt)
  elif hostCheck == 'O' or hostCheck == 'o':
    while time.time() < timer_end:
      incomingPkt = packetSniff()
      if incomingPkt[1] == HOST:
        pkts.append(incomingPkt) 
      
  print('\nIntercepted {} packets within a {} second search!'.format(len(pkts), answer))

  # creates the actual log excel file from the stored logs [note: this function replaces the current standing log file]
  print('\nCreating log...\n')

  createTrafficLog(pkts)
  print('\nCompleted log!\n')

  # notifies user of location of log file location and allows them to access it immediately after scan
  current = str(os.getcwd())

  print('You can find your log file at \n' + current + '\logs.xlsx' +'\n\n')
  openfile = input('Would you like to access the file now (Y/N)?: ')
  if openfile == 'Y' or openfile == 'y':
    print('\nOpening log...')
    os.system("start " + current + '\logs.xlsx')
    retry = input('\nWould you like to run would you like to run SniffyBoy again (Y/N)?: ')
    if retry == 'Y' or retry == 'y':
      # userInterface()
      print('grog')
    elif retry == 'N' or retry == 'n':
      print('Thank you for using SniffyBoy!')
      sys.exit()
  elif openfile == 'N' or openfile == 'n':
    print('Thank you for using SniffyBoy!')
    sys.exit()
  else:
    print('That is an invalid command. Exiting program...')
    sys.exit()

if __name__ == '__main__':
  sniffPref()