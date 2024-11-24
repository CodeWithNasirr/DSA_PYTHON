

def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        min_value=i
        for j in range(i+1,n):
            if list1[j]<list1[min_value]:
                min_value=j
        list1[i],list1[min_value]=list1[min_value],list1[i]
        

l=[9,8,7,6,5,4,3,2,1,0]
selection_sort(l)
print(l)