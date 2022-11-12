
# x = 'Global/BackOffice/Mclean/123 Street'

# l = x.split('/')
# l = l[2:]
# y = '/'.join(l)
# print(y)

keys = ['1','2','3','4']
dict = {}
for i in keys:
    dict.setdefault(i, '0')

print(dict.keys())