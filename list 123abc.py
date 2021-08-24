a=[1,2,3]
b=["a","b","c"]
i=0
c=[]
d=""
e=""
a=[1,2,3]
while i<len(a) and i<len(b):
    d=d+str(a[i])
    e=e+str(b[i])
    i+=1
f=d+e
c.append(f)
print(c)
    