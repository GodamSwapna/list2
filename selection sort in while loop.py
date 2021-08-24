list1=[12,8,3,20,11]
i=0
while i<len(list1):
    min_value=list1[i]
    j=0
    while j<len(list1)-1:
        if list1[j]<list1[min_value]:
            min_value=list1[j]
        list1[i],list1[min_value]=list1[min_value],list1[i]
        j+=1
    i+=1
print(list1)