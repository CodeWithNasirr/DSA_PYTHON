def Sum_N(n):
    if n==0:
        return 0
    return n + Sum_N(n-1)
x=Sum_N(5)
print(x)