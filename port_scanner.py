import socket
import sys
import datetime

# basic port scanner 
def portScan(port):
  HOST = ""
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.bind((HOST, port))
  except socket.error as e:
    print(str(e))

  s.listen(5)
  conn, addr = s.accept()

  print('Connected to: '+addr[0]+':'+addr[1])

portScan(80)