from testing import packetSniff
import time
import subprocess

def userInterface():
  subprocess.call('CLS', shell=True)
  answer = int(input('How many seconds do you want to run SniffyBoy for?: '))
  timer_end = time.time() + answer
  pkts=[]
  while time.time() < timer_end:
    pkts.append(packetSniff())
    

  print('Intercepted {} packets for {} seconds!'.format(len(pkts), answer))

if __name__ == "__main__":
  userInterface()