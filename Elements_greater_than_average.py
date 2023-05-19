a = int(input())
k = list(map(int,input().split()))
cv=0
c=0
for j in k:
    c+=j
d=c//a
for j in k:
    if d<=j:
        cv+=1
print(cv)
        