list1=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
i=0
list2=[]
while i<len(list1):
    if type(list1[i])==list:
        j=0
        while j<len(list1[i]):
            list2.append(list1[i][j])
            j+=1
    else:
        list2.append(list1[i])
    i+=1
print(list2)

