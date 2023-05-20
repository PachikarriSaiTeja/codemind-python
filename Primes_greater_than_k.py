def p(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a = int(input())
k = list(map(int,input().split()))
c = int(input())
g=0
e=0
m=[]
for i in k:
    if p(i) is True:
        m.append(i)
j = set(m)
for l in j:
    if l>=c:
        e+=1
print(e)


        
