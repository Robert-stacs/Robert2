n=int(input())
def fib(n):
    a=1
    b=1
    c=0
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    return c


z=fib(n)
print(z)