def p(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a = input()
b = a[::-1]
c = int(b)
d = int(a)
if(p(c)is True and p(d) is True):
    print("circular prime")
elif(p(d) is True and p(c) is False):
    print("prime but not a circular prime")
else:
    print('not prime')
