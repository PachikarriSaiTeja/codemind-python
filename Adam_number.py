a = input()
b = int(a)
c = a[::-1]
d = int(c)
e=d*d
g=str(e)
f=b*b
h=str(f)
if g==h[::-1]:
    print("True")
else:
    print("False")