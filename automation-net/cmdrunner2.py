#!/usr/bin/env python

import netmiko
import json
#connection to multiple devices
devices = '''
10.0.0.255
10.0.0.254
10.0.0.253
10.0.0.252
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'cisco'
password = 'cisco'

for device in devices:
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
#connects to device
connection
#prints the command
print(connection.send_command('sh ip int brief'))
#disconnects from device
connection.disconnect()