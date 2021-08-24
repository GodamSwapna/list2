a=[[2,7,6],[9,5,1],[4,3,8]]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(a):
    r1=r1+a[0][i]
    r2=r2+a[1][i]
    r3=r3+a[2][i]
    c1=c1+a[0][i]
    c2=c2+a[1][i]
    c3=c3+a[2][i]
    d1=d1+a[i][i]
    d2=d2+a[i][2-i]
    i+=1
if r1==r2==r3==c1==c2==c3==d1==d2:
    print("magic square")
else:
    print("not magic square")
    