n=int(input())
x=[int(j) for j in input().split()]
rep=[]
size=len(x)
for i in range(size):
  k=i+1
  for j in range(k,size):
    if x[i]==x[j] and x[i] not in rep:
      rep.append(x[i])
    else:
      print('unique')
      break
  break
      
rep.sort()
print(*rep)
  
