class router:
    '''router class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model             :{self.model}\n'\
               f'Software Version         :{self.swversion}\n'\
               f'Router Management Address:{self.ip_add}'
        return desc

class switch(router):
    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Switch Model             :{self.model}\n'\
               f'Software Version         :{self.swversion}\n'\
               f'Switch Management Address:{self.ip_add}'
        return desc

rtr1 = router('CSR1000V', '17.03.03', '10.10.10.1')
rtr2 = router('ISR4221', '16.9.5', '10.10.10.2')
sw1 = switch('Cat9300', '16.9.5', '10.10.10.3')



print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), '\n', sep='')
print('Sw1\n', sw1.getdesc(), sep='')