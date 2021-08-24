a='my name is swapna'
i=0
b=''
c=[]
while i<len(a)-1:
    b=b+a[i]
    if a[i]==' ':
        c.append(b)
        b=''
    i=i+1
print(c)
# sentence = 'This is a sentence'
# split_value = []
# tmp = ''
# for c in sentence:
#     if c == ' ':
#         split_value.append(tmp)
#         tmp = ''
#     else:
#         tmp += c
# if tmp:
#     split_value.append(tmp)
# print(split_value)