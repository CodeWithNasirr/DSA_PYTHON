def Sum_Od(n):
    if n==1:
        return 1
    
    return 2*n-1 + Sum_Od(n-1)

x=Sum_Od(5)
print(x)