a = int(input())
k = list(map(int,input().split()))
c=0
for i in k:
    if i==0 or i==1:
        c+=1
if c==a:
    print("True")
else:
    print("False")