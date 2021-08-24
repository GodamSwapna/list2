import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digit
s4=string.punctuation
strong_pw=input("enter you are strong pasword:")
s=[]
s=extend(list(s1))
s=extend(list(s2))
s=extend(list(s3))
s=extend(list(s4))
if strong_pw in s:
    print("strong password")
else:
    print("not strong password") 