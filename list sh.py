# name="Navgurukul"
# i=0
# newlist=[]
# c=0
# while i<len(name):
#     newlist.append(name[i])
#     c=c+1
#     i+=1
# print(newlist)
# print(c)
name="Navgurukul"
i=0
empty=[]
while i<len(name):
    j=0
    c=0
    while j<len(name):
        if name[j]==name[i]:
            c=c+1
        j+=1
    if [name[i],c] not in empty:
        empty.append([name[i],c])
    i+=1
    # if name[i] not in empty:
    #     empty.append([name[i],c])
print(empty)