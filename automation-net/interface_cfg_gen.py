hvac_range = input('hvac_range: ')
security_range = input('security_range: ')
user_range = input('user_range: ')

ranges = [
    {'int_range':hvac_range, 'description':'HVAC', 'vlan':'20'},
    {'int_range':security_range, 'description':'Security', 'vlan':'80'},
    {'int_range':user_range, 'description':'User', 'vlan':'100', 'voice_vlan':'200'}
]

for range in ranges:
    if range['int_range']=='':
        pass
    elif len(range) > 3:
        print('interface range ' + range['int_range'])
        print('description ' + range['description'])
        print('switchport access vlan ' + range['vlan'])
        print('switchport mode access')
        print('switchport voice vlan ' + range['voice_vlan'])
        print('spanning-tree portfast' + '\n')
    else:
        print('interface range ' + range['int_range'])
        print('description ' + range['description'])
        print('switchport access vlan ' + range['vlan'])
        print('switchport mode access' + '\n')

# print('Rtr1\n', rtr1.getdesc(), '\n', sep='')