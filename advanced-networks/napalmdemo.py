import napalm
import json

driver = napalm.get_network_driver('ios')

device = driver(hostname='192.168.73.159', username='cisco', password='cisco')

device.open()
print(device.getconfig(retrieve='running', full=False))
print(device.get_environment())
device.close()