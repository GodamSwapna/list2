list1=[3,4,6,2,0,0,0,0,6,7,6,9,10,0,0,0,7,4,4,0,0,0,0,5,3,2,9,7,1,0,0,0,0]
i=0
mainList=[]
list2=[]
while i<len(list1):
    if list1[i]==0:
        if len(list2)!=0:
            mainList.append(list2)
        list2=[]
    else:
        list2.append(list1[i])
    i+=1
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
        
    