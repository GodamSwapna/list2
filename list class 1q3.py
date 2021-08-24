
s= 'my name is swapna'
s1='e'
s2 = [] 
i = -1 
j = -1 
  
while ' ' in s[i + 1:]: 
    i= s.index(' ', i + 1) 
    s2.append(s[j+ 1:i]) 
    j = i
 
s2.append(s[j + 1:]) 
# s2.insert(2,'e')
print(s2) 