list1=[10,4,25,1,5]
i=1
while i<len(list1):
    current_element=list1[i]
    pos=i
    while current_element<list1[pos-i] and pos>0:
        list1[pos]=list1[pos-1]
        pos=pos-1
    list1[pos]=current_element
    i+=1
print(list1)