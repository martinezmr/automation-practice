x = ['ustxb41916sw01', 'ustxb41916sw02']

l = []
for i in x:
    j1 = i[:10] + 'sd01'
    j2 = i[:10] + 'sd02'
    l.append(j1)
    l.append(j2)

y= []
for i in l:
    if i not in y:
        y.append(i)

print(y)

j = []
j = j.append(' ')
print(j)