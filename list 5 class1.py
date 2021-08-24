a=[3,0,1,-1,-3,2,5]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)
    