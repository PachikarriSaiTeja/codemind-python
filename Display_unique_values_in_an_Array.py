a = int(input())
k=0
b = list(map(int, input().split()))
for I in b:
    if b.count(I)==1:
        print(I, end=" ")
        k+=1
if k==0:
    print(-1)