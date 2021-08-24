a=[[6,7,8],[3,5,7,],[8,9,2]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
k=0
while k<len(b):
    l=0
    while l<len(b):
        if b[k]<b[l]:
            b[k],b[l]=b[l],b[k]
        l+=1
    k+=1
print(b)
