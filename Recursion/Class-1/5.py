def even(n):
    if n>0:
        even(n-1)
        print(2*n,end=" ")

even(10)