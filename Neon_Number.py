a = int(input())
s = a*a
c=0
for i in range(s):
    d = s%10
    c+=d
    s = s//10
if c==a:
    print("Neon Number")
else:
    print("Not Neon Number")