chr=input("enter you are sentence:")
b=""
c=0
i=0
while i<len(chr):
    if (chr[i]>="a" and chr[i]<="z") or (chr[i]>="A" and chr[i]<="Z"):
        if chr[i] not in b:
            b=b+chr[i]
            c=c+1
    i+=1
if c==26:
    print("pangram")
else:
    print("not penagram")

        
