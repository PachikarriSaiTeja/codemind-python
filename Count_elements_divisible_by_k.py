a,c=map(int, input().split())
b = list(map(int, input().split()))
w=0
for i in b:
    if i%c==0:
        w+=1
print(w)