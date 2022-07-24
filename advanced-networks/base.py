from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time
from multiprocessing.dummy import Pool as ThreadPool
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import logging
import traceback
from datetime import datetime
import subprocess
import re
import pandas as pd
from openpyxl import Workbook, load_workbook

def read_devices(devices_filename):
    devices = {} # create our dictionary for storing devices and their info
    with open( devices_filename ) as devices_file:
        for device_line in devices_file:
            device_info = device_line.strip().split(',') # extract device info from line
            device = {'ipaddr': device_info[0],
                      'type': device_info[1]} # create dictionary of device objects
            devices[device['ipaddr']] = device # store our device in the devices diciontary
                                                # note the key for devices dictionary entries is ipaddr
    print('\n------devices----------------------')
    return devices

def config_worker(devices_and_creds):
    device = devices_and_creds
    username = eid
    creds = password
    #----Connect to the device
    if device['type'] == 'versa': device_type = 'flexvnf'

    elif device['type'] == 'cisco-ios': device_type = 'cisco_ios'

    else:                               device_type = 'cisco_ios' # default to cisco ios

    #----Connect to the device

    if device_type == 'cisco_ios':  # cisco commands follow

        print('-----Getting Config from Device----')
        try:

            session = ConnectHandler(device_type=device_type, ip=device['ipaddr'],
                        username=username, password=password, banner_timeout=400, global_delay_factor=4)

            #type cisco commands below
            hostname = session.send_command('sh run | i hostname')
            hostname = hostname.split()
            print(hostname)
        
        except NetMikoTimeoutException:
            print(f'Device Timeout for {device["ipaddr"]}')
            now = datetime.now()
            with open(f'exceptions.log', 'a+') as exc:
                exc.write(f'{device["ipaddr"]}) had a timeout exception at {now}.\n')
        
        except NetMikoAuthenticationException:
            print(f'Authentication failed for {device["ipaddr"]}')
            now = datetime.now()
            with open(f'exceptions.log', 'a+') as exc:
                exc.write(f'{device["ipaddr"]}) had an authentication exception at {now}.\n')

        except SSHException:
            print(f'SSH failed for {device["ipaddr"]}')
            with open(f'exceptions.log', 'a+') as exc:
                exc.write(f'{device["ipaddr"]}) had an SSH exception.\n')

        except Exception:
            print(f'Exception for {device["ipaddr"]}')
            with open(f'exceptions.log', 'a+') as exc:
                exc.write(f'{device["ipaddr"]}) had a general exception.  See log for more information.\n')
            logging.error(traceback.format_exc())

    return

# ------- MAIN: Get Configuration

eid = input('Username: ')
password = getpass()

devices = read_devices('devices-file.txt')
num_threads = 25

config_params_list = []
for ipaddr,device in devices.items():
    config_params_list.append( device )

starting_time = time()

print('\n--- Creating threadpoool, launching get config threads\n')
threads = ThreadPool( num_threads )
results = threads.map( config_worker, config_params_list )

threads.close()
threads.join()

print('\n---- End get config threadpool, elapsed time= ', time()-starting_time)