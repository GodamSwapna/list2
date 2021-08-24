print("*26")

list1=[4,5,5,5,3,8]
i=0
list2=list(set(list1))
while i<len(list2):
    j=0
    count=0
    while j<len(list1):
        if list1[j]==list2[i]:
            count+=1
        j+=1
    if count>=3:
        print(list2[i])
    i+=1