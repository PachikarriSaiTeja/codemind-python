p,r,t=map(int,input().split())
p = p*(1+r/100)**t
print('{0:.2f}'.format(p))
