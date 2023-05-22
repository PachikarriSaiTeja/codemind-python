a,b=map(int,input().split())
c=0
k = list(map(int, input().split()))
for i in k:
    if i%b!=0:
        c+=1
print(c)
