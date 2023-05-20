def p(x):
    y = x[::-1]
    if (x==y):
        return True
    else:
        return False
a = int(input())
b = int(input())
for i in range(a,b):
    if p(str(i)) is True:
        print(i,end=" ")
    