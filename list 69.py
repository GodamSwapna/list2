list1=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
i=0
newlist=[]
while i<len(list1):
    if list1[i] not in newlist:
        newlist.append(list1[i])
    i=i+1
print(newlist)
    # j=0
    # list2=[]
    # while j<len(list1[i]):

#         list2.append(list1([i][j]))
#         j+=1
#     # if list2 not in newlist:
#     #     newlist.append(list2[i])
#     # i+=1
# print(list2)