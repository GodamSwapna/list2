a=[[7,2,3,4,5,6],[1,2,3,4,5,6]]
i=0
j=1
c=[]
while i==0:
    k=0
    while k<len(a[i]):
        c.append(a[i][k]-a[j][k])
        k+=1
    i+=1
    j+=1
print(c)
i=0
j=1
k=0
l=[]
while k<len(a[i]):
    l.append(a[i][k]-a[j][k])
    k+=1
print(l)
