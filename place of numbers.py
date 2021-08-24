def calculate(num1):
    num=10**(int(str(len(num1)-1)))
    str1=""
    while num:
        if ((num1%num)*num)!=0:
            str1=str1+((num1%num)*num)+'+'
        num=num//10
    return [0::len(str1)-3]
num1=int(input("enter a number:"))
print(calculate(num1))
