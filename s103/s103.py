n=int(input())
l=[]
x=[int(i) for i in input().split()]
for i in range(n):
  if(x[i]==i):
    l.append(i)
print(*l)
   
