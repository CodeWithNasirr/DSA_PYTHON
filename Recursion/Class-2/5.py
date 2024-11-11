def Sum_Even(n):
    if n==0:
        return 0
    return n**2 + Sum_Even(n-1)


x=Sum_Even(5)
print(f"Sum of Even Number is : {x}")