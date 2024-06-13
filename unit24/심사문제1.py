import string

li=input().split()
c=0

for i in li:
    i=i.strip(string.punctuation)
    if i =='the':
        c+=1

print(c)
