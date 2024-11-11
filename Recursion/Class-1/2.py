def Rev(n):
    if n>0:
        print(n,end=" ")
        Rev(n-1)

Rev(10)