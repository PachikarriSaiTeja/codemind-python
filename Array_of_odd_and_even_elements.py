a = int(input())
k = list(map(int, input().split()))
n = [ ]
for i in k:
    if i%2!=0:
        n.append(i)
        print(i,end=" ")
for i in k:
    if i%2==0:
        n.append(i)
        print(i,end=" ")
   
 