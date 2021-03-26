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
t=int(input("число которое ну может надо найти"))
left=0
righa=len(a)-1
mid=(left+righa)//2
while a[mid]!=t:

	if a[mid]<t:
		left=mid+1
	if a[mid]>t:
		righa=mid-1
	mid=(left+righa)//2

	if a[mid]==t:
		print(mid)
	elif left>=righa:
		print("NET")
		break
print()
