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
b = int(input())
c=0
for i in range(a,b):
    if p(i) is True:
        print(i)