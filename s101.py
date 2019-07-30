n=int(input())
x=[int(j) for j in input().split()]
rep=[]
lis=[]
lis=x
size=len(x)
x=set(x)
x=list(x)
if(x==lis):
  print('unique')
else:
  for i in range(size):
    k=i+1
    for j in range(k,size):
      if lis[i]==lis[j] and lis[i] not in rep:
        rep.append(lis[i])
      
rep.sort()
print(*rep)
