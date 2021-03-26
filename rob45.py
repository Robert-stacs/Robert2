a=[5,5]
def mas(z):
    dvoech=False
    otl=True
    for i in range(len(z)):
        if z[i]==2:
          dvoech=True
        if z[i]!=5:
          otl=False
    if dvoech:
        print("Двоечник")
    if otl:
        print("Отличник")
mas(a)