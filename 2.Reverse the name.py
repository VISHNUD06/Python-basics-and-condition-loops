a=input('enter first name :')
b=input('enter second name :')
c=''
d=''
k=len(a)-1
l=len(b)-1
for i in range(k,-1,-1):
    c=c+a[i]
for j in range(l,-1,-1):
    d=d+b[j]
    rever_se=(c)+(' ')+(d)
print(rever_se)
    
