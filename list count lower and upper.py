chr=input("enter you are character:")
i=0
count_lower=0
count_upper=0
while i<len(chr):
    if chr[i]>="a" and chr[i]<="z":
        count_lower=count_lower+1
    else:
        count_upper=count_upper+1
    i+=1
print("count lower letters:",count_lower)
print("count upper letter:",count_upper)