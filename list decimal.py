b= [1, 0, 0, 1, 1, 0, 1, 1] 
sum=0
i=-1
while i>=-len(b):
    sum=sum+b[i]*2**-(i+1)
    i-=1
print(sum)
