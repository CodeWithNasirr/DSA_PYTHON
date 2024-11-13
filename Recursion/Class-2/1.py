def Sum_N(n):
    if n==1:
        return 1
    return n + Sum_N(n-1)
x=Sum_N(5)
print(x)