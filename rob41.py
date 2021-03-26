import random

z=int(input("Введите длину массива: "))
def mas(z):
    a=[]
    for i in range(z):
        n=random.randint(10,99)
        a.append(n)
    return a
def print_mas(a):
    for i in range(len(a)):
        print(a[i],end=",")
    print(a[len(a)-1],end=".")
    print()
arr = mas(z)
print_mas(arr)

