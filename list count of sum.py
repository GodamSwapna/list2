list1=[3,4,6,2,0,0,0,0,6,7,6,9,0,0,0,0,7,4,4,0,0,0,0,5,3,2,9,7,1,0,0,0,0]
mainList=[]
list2=[]
for i in list1:
    if i==0:
        if len(list2)!=0:
            mainList.append(list2)
        list2=[]
        continue
    else:
        list2.append(i)
i=0
newList=[]
while i<len(mainList):
    sum=0
    j=0
    while j<len(mainList[i]):
        sum=sum+int(mainList[i][j])
        j+=1
    newList.append(sum)
    i+=1
print(newList)
        
    