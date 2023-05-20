a = int(input())
k = list(map(int,input().split()))
c,d=map(int,input().split())
g=0
m=[]
for i in k:
    if i>=c and i<=d:
        g+=i
print(g)
    

        