pos_of_home=1
pos_of_apple=5
pos_of_orange=-3
oranges_fell_d=4
apple_fell_d=5
i=0
c_a=0
while i<apple_fell_d:
    direc=int(input("in wich direction apple fall down:"))
    p=pos_of_apple+direc
    if p==pos_of_home:
        c_a=c_a+1
    i+=1
print("apple are present in home:",c_a)
i=0
c_o=0
while i<oranges_fell_d:
    direc=int(input("how many oranges do you want:"))
    p=pos_of_orange+direc
    if p==pos_of_home:
        c_o=c_o+1
    i+=1
print(" oranges are  present in home:",c_o)
print("total apple and oranges present in home:",c_a+c_o)
