n="my name is navagurukul"
b=[]
i=0
m=input("enter a element:")
while i<len(n):
    element=""
    while True:
        if n[i] == m:
            b.append(element)
            b+=[n[i]]
            i+=1
            break
        else:
            element=element+n[i]
            i+=1
        # b.append(element)
        if i==len(n):
            b.append(element)
            break
print(b)

