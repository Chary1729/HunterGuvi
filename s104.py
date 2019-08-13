n=int(input())
mylist=[int(x) for x in input().split()]
for i in range(n):
  if mylist.count(i)==1:
    print(i)
  
