import random

a=[]
b=0
ae=int(input("Введите длину массива: "))
f=int(input("ведите максимальное число: "))
for i in range(ae):
    n=random.randint(1,f)
    a.append(n)
print(a)
flag=True
while flag:
	flag=False
	for i in range(len(a)-1):
		if a[i]>a[i+1]:
			flag=True
			b = a[i]
			a[i] = a[i+1]
			a[i+1] = b
	print(a)
