def merge_sort(list1):
    # Base condition: if the list contains 1 or no elements, it is already sorted
    if len(list1) > 1:
        # Find the middle index of the list
        mid = len(list1) // 2

        # Divide the list into left and right halves
        left_list = list1[:mid]
        right_list = list1[mid:]

        # Recursively sort both halves
        merge_sort(left_list)
        merge_sort(right_list)

        # Initialize pointers for left, right, and merged lists
        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
            else:
                list1[k] = right_list[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left list
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right list (corrected loop condition)
        while j < len(right_list): 
            list1[k] = right_list[j]
            j += 1
            k += 1


# Example list to sort
x = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Call the merge_sort function
merge_sort(x)

# Print the sorted list
print(x)
