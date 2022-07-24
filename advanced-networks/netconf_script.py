# this is an example (not usable)
from ncclient import manager
from virl_router_info import router

config_template = open(
    '/home/know/Documents/CodeSamples/Python/Networking/IOS-XE/ios_config.xml').read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Knox wuz here")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"]):
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)