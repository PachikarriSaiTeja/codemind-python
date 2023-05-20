a,b = map(int,input().split())
k = list(map(int,input().split()))
h = list(map(int,input().split()))
c=0
d=[]
for i in k:
    for j in h:
        if i not in h and j not in k:
            d.append(i)
            d.append(j)
        
e = set(d)
for s in e:
    c+=1
print(c)


