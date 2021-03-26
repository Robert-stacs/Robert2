n=int(input())
m=int(input())
c=1
v=1
b=1
for i in range(1,n+1):
    c=c*i
for i in range(1,m+1):
    v=v*i
for i in range(1,n-m+1):
    b=b*i
print(c/(v*b))
