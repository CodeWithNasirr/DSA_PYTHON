def Sum_N(n):
    if n==1:
        return 1
    return n + Sum_N(n-1)

print(Sum_N(5))