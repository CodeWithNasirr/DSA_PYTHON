import time  # Importing the time module to measure execution time

# Standard Bubble Sort Implementation
def bubble_sort(arg):
    start = time.time()  # Record the start time

    # Outer loop for number of passes
    for r in range(len(arg)):
        print(f"r->{r}")  # Debugging: Show the current pass number

        # Inner loop to compare adjacent elements
        for i in range(0, len(arg) - r - 1):  
            print(f"i->{i}")  # Debugging: Show the current index being compared

            # Swap if the current element is greater than the next
            if arg[i] > arg[i + 1]:  
                arg[i], arg[i + 1] = arg[i + 1], arg[i]  # Swap elements

    # Create a new list to store unique elements
    item = []
    for x in arg:  
        # Append only if the element is not already in the new list
        if x not in item:  
            item.append(x)

    end = time.time()  # Record the end time
    # Print the execution time (commented out for now)
    # print(f"Time taken: {end - start:.6f} seconds")

    return item  # Return the sorted list with unique elements


# Test the bubble_sort function
arg = [4, 22, 575, 3, 7, 157, 1, 45, 2, 14, 2, 4, 5, 75, 8, 9]
print(bubble_sort(arg))  # Output the sorted unique list


# Optimized Bubble Sort Implementation
def Mod_bubble_sort(arg):
    start = time.time()  # Record the start time

    # Outer loop for number of passes
    for r in range(1, len(arg)):  
        flag = False  # Initialize flag to track if any swaps occurred

        # Inner loop to compare adjacent elements
        for i in range(0, len(arg) - r):  
            # Swap if the current element is greater than the next
            if arg[i] > arg[i + 1]:  
                arg[i], arg[i + 1] = arg[i + 1], arg[i]  # Swap elements
                flag = True  # Set flag to True since a swap occurred

        # If no swaps occurred in this pass, break early (list is already sorted)
        if not flag:  
            break

    # Create a new list to store unique elements
    item = []
    for x in arg:
        # Append only if the element is not already in the new list
        if x not in item:
            item.append(x)

    end = time.time()  # Record the end time
    print(f"Time taken: {end - start:.6f} seconds")  # Output execution time
    return item  # Return the sorted list with unique elements


# Test the Mod_bubble_sort function
arg = [4, 22, 575, 3, 7, 157, 1, 45, 2, 14, 2, 4, 5, 75, 8, 9]
# Uncomment below to test the optimized bubble sort
# print(Mod_bubble_sort(arg))  # Output the sorted unique list
