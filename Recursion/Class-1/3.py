def odd(n):
    if n>0:
        odd(n-1)
        print(2*n-1,end=" ")

odd(10)