import socket
import sys
import datetime
import subprocess

def generateLANDevices():
  #runs arp in cmd to return users on network with IP and MAC
  output = subprocess.check_output(("arp", "-a"))
  decoded = output.decode("ASCII")
  formatTable = decoded[86:].lstrip().rstrip().split(' ')
  devices =[]
  for x in range(len(formatTable)):
    if formatTable[x].startswith('192.168'):
      devices.append(formatTable[x])
  print(decoded)


# discovering hostname from IP 
  for device in devices:
    try:
      print(socket.gethostbyaddr(device) + ' is using the IP address ' + device)
    except socket.herror:
      print("Can't find hostname for " + device)

if __name__ == '__main__':
  generateLANDevices()