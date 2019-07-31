n=int(input())
l=[]
c=0
x=[int(i) for i in input().split()]
for i in range(n):
  if(x[i]==i):
    l.append(x[i])

if(len(l)==0):
  print(-1)
else:
  print(*l)
