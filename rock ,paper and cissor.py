i=0
while i<3:
    n=input("do you want to play give me yes/no:")
    if n=="yes":
        player1=input("enter you  are chance:")
        player2=input("enter you are chance:")
        if player1=="rock" and player2=="paper":
            print("winner is paper")
        elif player1=="rock" and player2=="cissor":
            print("winner is rock")
        elif player1=="rock" and player2=="rock":
            print("you are tie")
        elif player1=="cissor" and player2=="paper":
            print("winner is cissor")
        elif player1=="cissor" and player2=="cissor":
            print("it is tie")
        elif player1=="paper" and player2=="paper":
            print("it is tie")
    else:
        print("skip the game")
    i+=1