a = int(input())
k = list(map(int,input().split()))
m=[ ]
for i in k:
    if(i%2!=0):
        m.append(i)
for i in k:
    if(i%2==0):
        m.append(i)
for j in m:
    print(j,end=' ')

        
    


    