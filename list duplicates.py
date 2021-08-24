a=[6,5,4,6,5,4,2,1]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)

b=list(set(a))
print(b)



