from pprint import pp

loopList = [1,2,3,4,5,6,7,8,9,10]

count = 0
variableNum = 1
data = []
while count <= len(loopList):
    sl = loopList[count:(count+4)]
    host ={
        f'access{variableNum}': sl
    }
    data.append(host)
    variableNum +=1
    count +=4

host = {}
x = ['a','b','c','d']
y = [1,2,3,4]

for i in range(len(x)):
        host[x[i]]= y[i]

pp(host)

x = ['b','a','c','x','d']

for i in x:
    try:
        print(host[i])
    except KeyError:
         print('No key')
    # if count > len(loopList):
    #     break




