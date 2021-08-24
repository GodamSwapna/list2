list1=[3, 4, 6,2 ,0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
i=0
list2=[]
list3=[]
while i<len(list1):
    if list1[i]!=0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
    i+=1
print(list2+list3)