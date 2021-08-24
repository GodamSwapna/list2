list1=[10,20,30]
list2=[40,50,60]
i=0
while i<len(list2):
	 list1.insert(i,list2[i])
	 i+=1
print(list1)