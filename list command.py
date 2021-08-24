endloop=int(input("enter you are ending loop here:"))
i=0
output=[]
while i<endloop:
    command=input("enter your command'append/insert/remove/pop/sort/reverse':")
    splcommand=command.split()
    print(splcommand)
    if splcommand[0]=="append":
        output.append(splcommand[1])
        print(output)
    elif splcommand[0]=="insert":
        output.insert(splcommand[1],splcommand[2])
        print(output)
    elif splcommand[0]=="remove":
        output.remove(splcommand[1])
        print(output)
    elif splcommand[0]=="pop":
        output.pop()
        print(output)
    elif splcommand[0]=="sort":
        output.sort()
        print(output)
    elif splcommand[0]=="reverse":
        output.reverse()
        print(output)
    elif i==endloop:
        print("you are choice is done")
    i+=1
