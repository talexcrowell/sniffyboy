from sniff_search import sniffPref 
  
def menu():
  print('\t\t\t|--- MENU ---|\n')
  print('[1] Packet Sniffer')
  print('[2] Port Scanner')
  print('[3] Information\n')
  menuChoice = int(input('Please select an option from the menu: '))
  if menuChoice == 1:
    sniffPref()
  elif menuChoice == 2:
    print("WIP...")
  elif menuChoice == 3:
    print('WIP...')
  