a=['red','orange','green','blue','white']
b=['black','yellow','green','blue']
i=0
a1=[]
while i<len(a): 
    if a[i] not in b:
        a1.append(a[i])
    i+=1
j=0
b1=[]
while j<len(b):
    if b[j] not in a:
        b1.append(b[j])
    j+=1
print(a1)
print(b1)
