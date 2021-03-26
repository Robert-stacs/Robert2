import math
a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
    print ("корней нет")
elif D==0:
    x=-b/(2*a)
    print ("1 корень")
    print (x)
else:
    y=(-b-math.sqrt(D))/(2*a)
    z=(-b+math.sqrt(D))/(2*a)
    print ("2 кореня")
    print (y)
    print (z)