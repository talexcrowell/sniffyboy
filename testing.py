# IP header
# raw sockets
# parse the IP header (struct)
# regular expressions

import socket
import sys
import struct
import re
import datetime
from protocols import protocols
from logs import createTrafficLog

def receiveData(socket):
  '''This function retrives data (intercepts package) from the socket'''
  data = ''
  try:
    data = socket.recvfrom(65565)
  except TimeoutError:
    data = ''
  except:
    print('An error has occured')
    sys.exc_info()
  return data[0]

#get the time of the service in 8 bits
def getTOS(data):
  precedence = {0: 'Routine', 1: "Priority", 2: 'Immediate', 3: 'Flash', 4: 'Flash override', 5: 'CRITIC?ECP', 6: 'Internetwork control', 7: 'Network control'}
  delay= {0: 'Normal delay', 1: 'Low Delay'}
  throughput = {0:'Normal throughput', 1: 'High throughput'}
  reliability = {0: 'Normal reliability', 1: 'High reliability'}
  cost = {0: 'Normal monetary cost', 1: 'High monetary cost'}

  D = data & 0x10
  D >>= 4
  T = data & 0x8
  T >>= 3
  R = data & 0x4
  R >>= 2
  M = data & 0x2
  M >>= 1

  tabs = '\n\t\t\t'
  TOS = precedence[data >> 5] + tabs + delay[D] + tabs + throughput[T] + tabs + reliability[R] + tabs + cost[M]
  return TOS

def getFlags(data):
  flagR = {0: 'Reserved bit'}
  flagDF = {0: 'Fragment if necessary', 1: 'Do not fragment'}
  flagMF = {0:'This is the last fragment', 1: 'More fragments follow'}
  R = data & 0x8000
  R >>= 15
  DF = data & 0x4000
  DF >>= 14
  MF = data & 0x2000
  MF >>= 13

  tabs = '\n\t\t\t'
  flags = flagR[R] + tabs + flagDF[DF] + tabs + flagMF[MF]
  return flags

def getProtocol(protocolNum):
  for protocol in protocols:
    if protocol == protocolNum:
      return protocols[protocol]
  else:
    return 'No such protocol was found'

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

data = receiveData(s)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])

version_IHL = unpackedData[0] 
version = version_IHL >> 4
IHL = version_IHL & 0xF
TOS = unpackedData[1]
totalLength = unpackedData[2]
ID = unpackedData[3]
flags = unpackedData[4]
fragmentOffest = unpackedData[4] & 0x1FFF
TTL = unpackedData[5]
protocolNum = unpackedData[6]
checksum = unpackedData[7]
sourceAddress = socket.inet_ntoa(unpackedData[8])
destinationAddress = socket.inet_ntoa(unpackedData[9])

log = ([
  ID, 
  sourceAddress,
  destinationAddress,
  getProtocol(protocolNum),
  getTOS(TOS),
  getFlags(flags),
  fragmentOffest,
  TTL,
  version,
  checksum,
  IHL*4,
  totalLength,
  str(data),
  str(data)[20:],
  str(datetime.datetime.now()).replace(' ', '-')[:19]
])

createTrafficLog(log)

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
  print("An IP packet with the size %i was captured.\n" % totalLength)
  print('Raw data: \n' + str(data))
  print("\nParsed Data")
  print("Version:\t\t" + str(version))
  print("Header Length:\t\t" + str(IHL*4) + ' bytes')
  print("Type of Service:\t" + getTOS(TOS))
  print("Length:\t\t\t" + str(totalLength))
  print('ID:\t\t\t' + str(hex(ID) + ' (' + str(ID) + ')'))
  print('Flags:\t\t\t' + getFlags(flags))
  print('Fragment offeset:\t' + str(fragmentOffest))
  print('TTL\t\t\t' + str(TTL))
  print('Protocol:\t\t' + getProtocol(protocolNum))
  print('Checksum:\t\t' + str(checksum))
  print('Source:\t\t\t' + sourceAddress)
  print('Destination:\t\t' + destinationAddress)
  print('Payload:\n' + str(data)[20:])

