# from pprint import pprint


# show_mac = [
#     {
#         "d_a": "5.5.5.5",
#         "d_p": "gi1",
#         "type": "dynamic",
#         "vlan": "1",
#         "device": 'R1'
#     },
#     {
#         "d_a": "6.6.6.6",
#         "d_p": "gi2",
#         "type": "dynamic",
#         "vlan": "2",
#         "device": 'R1'
#     },
#     {
#         "d_a": "7.7.7.7",
#         "d_p": "gi3",
#         "type": "dynamic",
#         "vlan": "3",
#         "device": 'R2'
#     }
# ]

# devicelist = []

# for i in show_mac:
#     d = i["device"]
#     devicelist.append(d)

# devicelist = list(set(devicelist))

# r = len(devicelist)
# dict = {}

# for x in range(0, r, 1):
#     c = []
#     for i in show_mac:
#         if i["device"] == devicelist[x]:
#             device = devicelist[x]
            
#             c.append(i)
#             dict[device] = c
            

# pprint(dict)
# print(len(dict))
            
# nums = (55,44,33,22)

# # print(max(min(nums[:2],abs(-42))))
# print(nums[:2])

text = "hello"

dict = {}

for i in text:
    if i not in dict.keys():
        dict[i] = text.count(i)

print(dict)