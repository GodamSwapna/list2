a=[[1,2,3,4],[5,6,7,8]]
i=0
list1=[]
while i<len(a):
    j=-1
    list2=[]
    while j>-5:
        list2.append(a[i][j])
        j-=1
    list1.append(list2)
    i+=1
print(list1)