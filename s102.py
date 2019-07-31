n=int(input())
x=[x for x in input().split()]
x=sorted(x,reverse=True)
for i in x:
  if i==0:
    print(0)
    break
  else:
    print(''.join(x))
    break
