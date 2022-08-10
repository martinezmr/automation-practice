import napalm
import json
from pprint import pprint

driver = napalm.get_network_driver('ios')

device = driver(hostname='192.168.73.159', username='cisco', password='cisco')

device.open()
pprint(device.get_config(retrieve='running', full=False))
pprint(device.get_environment())
device.close()