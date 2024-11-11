def Revodd(n):
    if n>0:
        print(2*n-1,end=" ")
        Revodd(n-1)

Revodd(10)