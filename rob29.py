a=int(input())
n=0
while a!=0:
    n+=a%10
    a=a//10
print(n)