n=int(input())
x=[int(x) for x in input().split()]
x.sort(reverse=True)
for i in x:
  if i==0:
    print(0)
    break
  else:
    print(i,end="")
