n=int(input())
for i in range(n):
  for j in range(n):
    if (i >= j and i <= n-1-j) or (i <= j and i >= n-1-j)  :
      print ('*',end='')
    else:
      print ('·',end='')
  print()