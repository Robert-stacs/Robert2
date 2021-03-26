import random
z= int(input())
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
min=99
max=0
for i in range(len(arr)):
    if  min>arr[i]:
        min=arr[i]
    if  max<arr[i]:
        max=arr[i]
print(min,max)