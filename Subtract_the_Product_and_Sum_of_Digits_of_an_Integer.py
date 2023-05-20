a = int(input())
b = str(a)
k=[]
p=1
s=0
while a!=0:
    d=a%10
    s+=d
    p*=d
    a=a//10
print(p-s)