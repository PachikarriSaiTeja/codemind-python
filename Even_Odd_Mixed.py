a = int(input())
b = str(a)
k=[ ]
ce,co=0,0
while a!=0:
    d = a%10
    k.append(d)
    a = a//10
for i in k:
    if i%2==0:
        ce+=1
    else:
        co+=1
for i in k:
    if ce==len(k):
        print("Even")
        break
    elif co==len(k):
        print("Odd")
        break
    else:
        print("Mixed")
        break