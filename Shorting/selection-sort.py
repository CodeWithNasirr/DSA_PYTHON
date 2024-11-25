

# Function to perform selection sort
def selection_sort(list1):
    # Get the length of the list
    n = len(list1)
    
    # Outer loop iterates through the entire list
    for i in range(n):
        # Assume the current index `i` has the minimum value
        min_value = i

        # Inner loop finds the smallest element in the remaining unsorted portion
        for j in range(i + 1, n):
            # If a smaller value is found, update `min_value` to this index
            if list1[j] < list1[min_value]:
                min_value = j

        # Swap the smallest value found with the value at index `i`
        # This places the smallest value in its correct position
        list1[i], list1[min_value] = list1[min_value], list1[i]

# Test list
l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Call the selection_sort function
selection_sort(l)

# Print the sorted list
print(l)
