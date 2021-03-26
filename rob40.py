import random

a=[]
z=int(input("Введите длину массива: "))
for i in range(z):
    n=random.randint(10,99)
    a.append(n)

for i in range(z-1):
    print(a[i],end=",")
print(a[z-1],end=".")
