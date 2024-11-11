def RevEven(n):
    if n>0:
        print(2*n,end=" ")
        RevEven(n-1)

RevEven(100)