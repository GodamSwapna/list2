n=int(input("enter power of number number:"))
num=int(input("entr a number:"))
sum=0
temp=num
while num>0:
        rem=num%10
        sum=sum+rem**n
        num=num//10
if sum==temp:
    print("given number is armstrong number")
else:
    print("given number is not armstrong number")