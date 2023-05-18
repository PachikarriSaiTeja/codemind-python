a = int(input())
k = list(map(int,input().split()))
c=0
for i in k:
    c+=i
p=(c/a)
print("{:.2f}".format(p))
    