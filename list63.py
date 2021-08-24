list1=[1,2,3,4]
str1="emp"
i=0
list2=[]
while i<len(list1):
    list2.append(str1+str(list1[i]))
    i+=1
print(list2)