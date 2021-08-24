list1=['abcd','abc','bcd','bkie','cdsw','sdfsd','dagfa','acjd']
i=0
list2=[]
list3=[]
list4=[]
while i<len(list1):
    if list1[i][0]=="a":
        list2.append(list1[i])
    if list1[i][0]=="d":
        list3.append(list1[i])
    if list1[i][0]=="w":
        list4.append(list1[i])
    i+=1
print(list2)
print(list3)
print(list4)