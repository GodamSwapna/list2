a=[2,8,-6,5,-1,7]
i=0
b=[]
while i<len(a):
	if a[i]<0:
	    b.append(0)
	else:
	    b.append(a[i])
	i+=1
print(b)