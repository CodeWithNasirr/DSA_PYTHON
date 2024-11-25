def quick_sort_iterative(l):
    if len(l) < 2:
        return l  # No sorting needed for empty or single-element lists

    stack = [(0, len(l) - 1)]  # Stack to store the start and end indices of sublists

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue  # Skip if the sublist has one or no elements

        pivot = l[start]  # Choose the pivot as the first element
        left = start + 1
        right = end

        # Partition the list
        while left <= right:
            while left <= right and l[left] <= pivot:
                left += 1
            while left <= right and l[right] > pivot:
                right -= 1
            if left < right:
                l[left], l[right] = l[right], l[left]  # Swap elements

        # Place the pivot in its correct position
        l[start], l[right] = l[right], l[start]

        # Push left and right sublists onto the stack
        stack.append((start, right - 1))
        stack.append((right + 1, end))

    return l


l = [9, 8, 7, 6, 21, 41, 53, 33, 12, 5, 4, 3, 2, 1, 0]
list1 = quick_sort_iterative(l)
print(list1)
