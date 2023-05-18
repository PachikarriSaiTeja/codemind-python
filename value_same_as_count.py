a = int(input())
k = list(map(int,input().split()))
c=[]
for i in k:
    if k.count(i)==i:
        c.append(i)
z=set(c)
print(len(z))
   
        


    