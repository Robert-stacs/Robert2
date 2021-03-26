n=int(input())
m=int(input())
def fact(n):
    tmp=1
    for i in range(1,n+1):
        tmp=tmp*i
    return tmp

print(fact(n)/(fact(m)*fact(n-m)))