# meraki script for lab envirorment
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '050f06ef01af496f7fe6c9fe58199775d276dbfa' # meraki token
meraki = MerakiSdkClient(token) # handles auth and storing of token for requests

orgs = meraki.organizations.get_organizations()
print(orgs)

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

params={}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params)
pprint(networks)

for network in networks:
    if network['name'] == 'DevNet Always On Read Only':
        netId = network['id']

vlans = meraki.vlans.get_network_vlans(netId)
vlan = vlans[0]
vlan['name'] = 'Manny was here'

updated_vlan = {}
updated_vlan['network_id'] = netId
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan

result = meraki.vlans.update_network_vlan(updated_vlan)

result_vlan = meraki.vlans.get_network_vlans(netId)
pprint(result_vlan)
