a  = int(input())
b = str(a)
c = a*a
d = str(c)
for i in d:
    if b in d:
        print("Automorphic Number")
        break
    else:
        print("Not an Automorphic Number")
        break