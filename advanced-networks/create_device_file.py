import re

i = 1 #input first IP for last octect
while i < 10: #input last IP +1 for last octet
    ipaddr = '192.168.73.' + str(i)
    device_type = 'cisco_ios'
    print(ipaddr + ',' + device_type)
    i += 1
    