import random
lst = []
for i in range (10):
    number = random.randint(0,101)
    lst.append(number)
print(lst)
S=1
f=open('hzrt13.txt','w')
for i in range(10):
    if(lst[i]%5!=0):
        f.write(str(lst[i]) + ' ')
        S= S * lst[i]
f.write('\n'+str(S))
f.close()
