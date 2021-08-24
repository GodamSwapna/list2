list1= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
str1=""
while i<len(list1):
    j=0
    while j<len(list1[i]):
        str1=str1+str(list1[i][j])
        j+=1
    i+=1
print(str1)