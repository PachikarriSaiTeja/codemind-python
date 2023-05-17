a = int(input())
b = str(a)
c=0
for i in b:
    if b.count(i)==1:
        c+=1
if c==len(b):
    print("Unique Number")
else:
    print("Not Unique Number")
       
        