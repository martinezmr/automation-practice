#!/usr/bin/env python

import netmiko
import json
#connection to multiple devices
devices = '''
192.168.73.131
192.168.73.133
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'cisco'
password = 'cisco'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
    try:
        print('~'*79)
        print('Connecting to device', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        print(connection.send_command('sh ip int brief'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)