import random
import time
print(time.ctime())
z=30
def mas(z):
    a=[]
    for i in range(z):
        n=random.randint(-1,7)
        a.append(n)
    return a
def print_mas(a):
    for i in range(len(a)-1):
        print(a[i],end=",")
    print(a[len(a)-1],end=".")
    print()
def cold_month(z):
    холодно=False
    for i in range(len(z)):
        if z[i]<0:
          холодно=True
    if холодно:
        print("холодно")

a = mas(30)
print_mas(a)
cold_month(a)