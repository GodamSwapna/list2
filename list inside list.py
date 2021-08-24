# a=[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     c=[]
#     while j<len(a):
#         if a[j]==a[i]:
#             c.append(a[j])
#         j+=1
#     if c not in b:
#         b.append(c)
#     i+=1
# print(b)


n=int(input("enter a number:"))
i=0
while i<10:
    # print('2 ','*',(i/2),'=',2*i//
    print(n, "*", i,"=" ,n*i)
    i+=.5
