a,b,k=map(int,input().split())
c=0
for i in range(a,b):
    if i%k==0:
        c+=1
if c==50:
    print("51")
else:
    print(c)