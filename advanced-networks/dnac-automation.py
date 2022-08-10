from dnacentersdk import api
import json
import time
import calendar

dna = api.DNACenterAPI(base_url = 'https://sandboxdnac.cisco.com',
username = 'devnetuser', password='Cisco123!', verify=False)

sites = dna.networks.get_site_topology()
for site in sites.response.sites:
    if site.parentId == '':
        print(site.name)
        for child_sites in sites.response.sites:
            if child_sites.parentId == site.id:
                print(f'  {child_sites.name}')
            for more_children in sites.response.sites:
                if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                    print(f'  {more_children.name}')