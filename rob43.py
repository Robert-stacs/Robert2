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
n = int(input("Введите число:"))
z=[]
for i in range(len(arr)):
    if n==arr[i]:
        z.append(i)
if z==[]:
    print("числа в массиве нет")
else:
    print(z)
