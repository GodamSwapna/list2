i=100
while i<=500:
    num=i
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem**3
        num=num//10
    if sum==i:
        print(sum,"is armstrong number")
    i=i+1