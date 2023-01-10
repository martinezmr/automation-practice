# x = ['ustxb41916sw01', 'ustxb41916sw02']

# l = []
# for i in x:
#     j1 = i[:10] + 'sd01'
#     j2 = i[:10] + 'sd02'
#     l.append(j1)
#     l.append(j2)

# y= []
# for i in l:
#     if i not in y:
#         y.append(i)

# print(y)

# j = []
# j = j.append(' ')
# print(j)
import re

l = ["switch11", "switch121"]

for i in l:
    floor = i[-3:]
    floor = f"{floor[0:- 1]}D"
    floor = re.sub('[^0-9]', '', floor)
    print(f"floor {floor}")

x = [1,2,3,4,5,6,7]
print(x[-2:])