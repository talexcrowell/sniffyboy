import testing
import time

def userInterface():
  answer = int(input('How many seconds do you want to run SniffyBoy for?: '))
  timer_end = time.time() + answer
  pktCount = 0
  while time.time() < timer_end:
    testing
    pktCount += 1

  print('Intercepted {} packets for {} seconds!'.format(pktCount, answer))

if __name__ == "__main__":
  userInterface()