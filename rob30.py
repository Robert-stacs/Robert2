a=int(input())
n=a%1000
t=a//1000
c=0
x=0
while n!=0:
    c+=n%10
    n=n//10
while t!=0:
    x+=t%10
    t=t//10
if (c==x):
  print('кушай')
else:
  print('не кушай')
print()
