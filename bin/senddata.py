#!/usr/bin/env python

# https://dzone.com/articles/python-getting-data-graphite-0

import platform
import socket
import time
import Adafruit_DHT as dht


CARBON_PORT = 2003

file = open('/home/pi/tempreport/etc/graphite_host_addr.dat')
for line in file:
    fields = line.strip().split()
    szGraphiteHostAddr = fields[0]
file.close()


szFqdn = platform.node()
arHostSplit = szFqdn.split(".")
szHostname = arHostSplit[0]

h,t = dht.read_retry(dht.DHT22, 4)
file = open('/home/pi/tempreport/etc/adjust.dat')
for line in file:
    fields = line.strip().split()
file.close()
fTemp = t + float(fields[0])
fHumidity = h + float(fields[1])
print ('Adjusted - Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(fTemp, fHumidity))

# The number before ':' is the 0-based index of the values of the .format() list
temperature_message = '{0:s}.temperature {1:0.1f} {2:d}\n'.format(szHostname, fTemp, int(time.time()))
humidity_message = '{0:s}.humidity {1:0.1f} {2:d}\n'.format(szHostname, fHumidity,  int(time.time()))

sock = socket.socket()
sock.connect((szGraphiteHostAddr, CARBON_PORT))
sock.sendall(temperature_message)
sock.sendall(humidity_message)
sock.close()
