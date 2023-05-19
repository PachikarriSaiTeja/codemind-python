a = int(input()) 
k = list(map(int, input().split()))
c=0
b =[]
for i in k:
    if i==k.count(i):
        b.append(i)
d = set(b)
for j in d:
    c+=1
print(c)
        
