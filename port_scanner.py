import socket
import sys
import datetime

HOST = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# basic specific port scan and listen
def portScanAndListen(port):
  try:
    s.bind((HOST, port))
  except socket.error as e:
    print(str(e))

  s.listen(5)
  conn, addr = s.accept()

  print('Connected to: '+addr[0]+':'+str(addr[1]))

def portScanner(port):
  try:
    s.connect(("localhost", port))
    return True
  except:
    return False

# for x in range(1,24):
#   if portScanner(x):
#     print('Port {} is open'.format(x))

for port in range(1, 80):
  res = s.connect_ex(('127.0.0.1', port))
  if res == 0:
    print('Port {}: Open'.format(port))
  s.close()