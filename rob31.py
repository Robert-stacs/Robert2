import random
n=random.randint(1,100)
a=int(input())
r=0
while a!=n:
    if a>n:
        print("меньше")
    else:
        print("больше")
    r=r+1
    a=int(input())
    if a==n:
        print("да")
print("кол-во подбора "+str(r))