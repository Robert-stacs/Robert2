n = int(input())
f = int(input())

def cl(n,f):
    for i in range(f):
        k = 0
        for i in range(n, 0, -2):
            for l in range(k):
                print(" ", end='')
            k = k+1
            for j in range(i):
                print("*", end='')
            print()
        k = k-2
        for i in range(3, n+2, 2):

            for l in range(k):
                print(" ", end='')
            k = k-1
            for j in range(i):
                print("*", end='')

            print()

cl(n,f)