i=0
list1=[]
while i<5:
    command=input("enter your command here:")
    if command=="append":
        n=(input("enter you are value:"))
        list1.append(n)
        print(list1)
    elif command=="insert":
        c=input("enter you item:")
        d=int(input("enter you are index:"))
        list1.insert(d,c)
        print(list1)
    elif command=="sort":
        list1.sort()
    elif command=="count":
        list1.count()
    elif command=="reverse":
        list1.reverse()
    elif command=="length":
        print(len(list1))
    elif command=="pop":
        print(list1.pop())
    else:
        print("you are choice is done")
    i+=1
print(list1)
