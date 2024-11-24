import time

def bubble_sort(arg):
    start=time.time()
    for r in range(len(arg)):
        print(f"r->{r}")
        for i in range(0,len(arg)-r-1):
            print(f"i->{i}")
            if arg[i]>arg[i+1]:
                arg[i],arg[i+1]=arg[i+1],arg[i]
    item=[]
    for x in arg:
        if x not in item:
            item.append(x)
    end = time.time()
    # print(f"Time taken: {end - start:.6f} seconds")
    return item
    

arg=[4,22,575,3,7,157,1,45,2,14,2,4,5,75,8,9]
print(bubble_sort(arg))


def Mod_bubble_sort(arg):
    start=time.time()
    flag=False
    for r in range(1,len(arg)):
        flag=False
        for i in range(0,len(arg)-r):
            if arg[i]>arg[i+1]:
                arg[i],arg[i+1]=arg[i+1],arg[i]
                flag=True
        if not flag:
            break
    item=[]
    for x in arg:
        if x not in item:
            item.append(x)
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")
    return item
    

arg=[4,22,575,3,7,157,1,45,2,14,2,4,5,75,8,9]
# print(Mod_bubble_sort(arg))