import random
z=10
def mas(z):
    a=[]
    for i in range(z):
        n=random.randint(10,99)
        a.append(n)
    return a
def print_mas(a):
    for i in range(len(a)-1):
        print(a[i],end=",")
    print(a[len(a)-1],end=".")
    print()
arr = mas(z)
print_mas(arr)

def maz2(arr):
    a=0
    for i in range(z):
        a+=arr[i]
    return a
print(maz2(arr))
