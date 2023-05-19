a = int(input())
b = list(map(int,input().split()))
d=0
v = 0
for i in b:
    d+=i
av=d//a
for i in b:
    if av>=i:
        v+=1
print(v)
        
   