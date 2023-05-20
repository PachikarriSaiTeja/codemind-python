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
cn=0
for i in range(1,a):
    if a%i==0:
        if p(i) is False:
            cn+=1
print(cn+1)
            