from sniff_search import sniffPref 
from discover_network import generateLANDevices
  
def menu():
  print('\t\t\t|--- MENU ---|\n')
  print('[1] Packet Sniffer')
  print('[2] Discover Network Devices')
  print('[3] Information\n')
  menuChoice = int(input('Please select an option from the menu: '))
  if menuChoice == 1:
    sniffPref()
  elif menuChoice == 2:
    generateLANDevices()
  elif menuChoice == 3:
    print('WIP...')
  