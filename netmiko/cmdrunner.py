#/usr/bin/env python

import netmiko
import json
#connection variable below
connection = netmiko.ConnectHandler(ip='192.168.73.131', device_type='cisco_ios', username='cisco', password='cisco')
#connects to device
connection
#prints the command
print(connection.send_command('sh ip int brief'))
#disconnects from device
connection.disconnect()