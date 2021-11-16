
l=[]

for i in range(2000,3101):
    if i%7==0:
        l.append(i)
for j in l:
    if j%5==1:
        
        print(j,',',end='')
