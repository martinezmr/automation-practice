#!/usr/bin/env python

import netmiko
import json
#connection to multiple devices
r1 = {'ip': '192.168.73.131',
        'device_type': 'cisco_ios',
        'username': 'cisco',
        'password': 'cisco'}

r2 = {'ip': '192.168.73.133',
        'device_type': 'cisco_ios',
        'username': 'cisco',
        'password': 'cisco'}

devices = [r1, r2]

device_type = 'cisco_ios'
username = 'cisco'
password = 'cisco'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
    try:
        print('~'*79)
        print('Connecting to device', device)
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('sh ip int brief'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)