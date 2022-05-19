#!/usr/bin/env python
#creates multiple files from output commands
from __future__ import absolute_import, division, print_function

import netmiko
import json
import mytools
import sys
import signal
import os

signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl-C



if len(sys.argv) < 3:
    print('Usage: cmdrunner.py commands.txt devices.json')
    exit()

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

username, password = mytools.get_credentials()

with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

with open(sys.argv[2]) as dev_file:
    devices = json.load(dev_file)

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print('~'*79)
        print('Connecting to device', device['ip'])
        connection = netmiko.ConnectHandler(**device)
        newdir = connection.base_promptos.mkdir(newdir)
        os.mkdir(newdir)
        for command in commands:
            filename = command.replace(' ', '_') + ' .txt'
            filename = '/'.join((newdir, filename))
            with open(filename, 'w') as out_file:
                    out_file.write(connection.send_commands(command) + '\n')
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device['ip'], e)