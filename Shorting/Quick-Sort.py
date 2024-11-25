def quick_sort(l):
    # Base case: if the list has zero or one element, it's already sorted.
    if len(l) < 1:
        return l
    else:
        # Choose the first element as the pivot
        pivot = l[0]
        
        # Create a list of elements less than or equal to the pivot
        lesser = [x for x in l[1:] if x <= pivot]
        
        # Create a list of elements greater than the pivot
        greater = [x for x in l[1:] if x > pivot]
        
        # Recursively sort the lesser and greater lists
        # Combine the sorted lesser list, the pivot, and the sorted greater list
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


# Input list to be sorted
l = [9, 8, 7, 6, 21, 41, 53, 33, 12, 5, 4, 3, 2, 1, 0]

# Call the quick_sort function and store the result in list1
list1 = quick_sort(l)

# Print the sorted list
print(list1)
