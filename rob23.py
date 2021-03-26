n=int(input())
for i in range(n):
  for j in range(n):
    if   i >= n-1-j :
      print ('*',end='')
    else:
      print ('.',end='')
  print()