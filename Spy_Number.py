a = int(input())
p=1
s=0
while a!=0:
    d=a%10
    s+=d
    p*=d
    a=a//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")