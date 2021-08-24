n=[50,40,23,70,56,12,5,10,7]
count=0
i=0
while i<len(n):
    if n[i]>20 and n[i]<40:
        count+=n[i]
    i+=1
print(count)