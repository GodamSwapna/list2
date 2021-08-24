i=0
a=[]
while i<=20:
    j=1
    b=[]
    while j<=5:
        b.append(j+i)
        j+=1
    a.append(b)
    i+=5
print(a)
#  nested listconvert single list
a=[1,2,[3,4,5,6],7,8,[9,10],11,12,[0,-1,-2,-3],[-2,-3,-5],[-6,-7,-8],0,1,[1,2,3]]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)      


