list1=[12,34,56,78]
i=0
newlist=[]
while i<len(list1):
    j=list1[i]
    sum=0
    while j>0:
        r=j%10
        sum=sum+r
        j=j//10
    newlist.append(sum)
    i+=1
print(newlist)

