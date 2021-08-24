chr="swapna is doing functions questions on python she is well"
chr1=input("enter you are sentence:")
chr3=chr.split()
i=0
count=0
while i<len(chr3):
    if chr3[i]==chr1:
        count=count+1 
    i+=1
print(chr1,count)
        