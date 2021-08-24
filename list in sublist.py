a=[2,4,5,6,1]
i=0
b=[]
while i<len(a):
    n=int(input("enter a number:"))
    b.append(a[i:i+n])
    i+=1
print(b)

