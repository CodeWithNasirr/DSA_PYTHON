# Function to perform insertion sort
def insertion_sort(list1):
    # Start from the second element (index 1), since the first element (index 0) is already "sorted"
    for i in range(1, len(list1)):
        temp = list1[i]  # Store the current element in a temporary variable
        j = i - 1  # Initialize the pointer for the sorted portion of the list

        # Move elements in the sorted portion (left side) that are greater than `temp` one position to the right
        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j]  # Shift the larger element to the right
            j -= 1  # Move to the previous element in the sorted portion

        # Insert the `temp` value at the correct position in the sorted portion
        list1[j + 1] = temp

# Test list
l = [9, 8, 87, 6543, 2, 55, 57, 1]

# Call the insertion_sort function
insertion_sort(l)

# Print the sorted list
print(l)


# In **Insertion Sort**, every new element (`temp`) is compared with all elements in the sorted part of the list **from right to left** (largest to smallest). This is why `2` gets compared with `6543`, `87`, `9`, and `8` one by one.

# Here’s how the **comparison process** works in the `while` loop when `temp = 2`:

# 1. **Start of the iteration (`j = 3`)**:
#    - `j` is the index of the last element in the sorted part (`6543` in `[8, 9, 87, 6543]`).
#    - Compare `2` with `list1[j]`:
#      - Is `2 < 6543`? Yes.
#      - Shift `6543` to the right: `[2, 8, 9, 87, 6543, 55, 57, 1]` becomes `[8, 9, 87, 6543, 6543, 55, 57, 1]`.
#      - Decrement `j` to `2`.

# 2. **Next comparison (`j = 2`)**:
#    - Compare `2` with `list1[j]` (`87`):
#      - Is `2 < 87`? Yes.
#      - Shift `87` to the right: `[8, 9, 87, 6543, 6543, 55, 57, 1]` becomes `[8, 9, 87, 87, 6543, 55, 57, 1]`.
#      - Decrement `j` to `1`.

# 3. **Next comparison (`j = 1`)**:
#    - Compare `2` with `list1[j]` (`9`):
#      - Is `2 < 9`? Yes.
#      - Shift `9` to the right: `[8, 9, 87, 87, 6543, 55, 57, 1]` becomes `[8, 9, 9, 87, 6543, 55, 57, 1]`.
#      - Decrement `j` to `0`.

# 4. **Next comparison (`j = 0`)**:
#    - Compare `2` with `list1[j]` (`8`):
#      - Is `2 < 8`? Yes.
#      - Shift `8` to the right: `[8, 9, 9, 87, 6543, 55, 57, 1]` becomes `[8, 8, 9, 87, 6543, 55, 57, 1]`.
#      - Decrement `j` to `-1`.

# 5. **End of comparisons (`j = -1`)**:
#    - Since `j < 0`, the `while` loop stops.
#    - Insert `2` into its correct position: `list1[j + 1] = 2`.

# Result after this step: `[2, 8, 9, 87, 6543, 55, 57, 1]`.

# ### Why Does It Compare with All Sorted Elements?
# - The `while` loop ensures that `temp` is compared with every element in the sorted part until it finds a smaller value or reaches the beginning of the list.
# - This behavior is controlled by:
#   ```python
#   while j >= 0 and temp < list1[j]:
#   ```
#   - `j >= 0` ensures it doesn’t compare beyond the leftmost element.
#   - `temp < list1[j]` ensures it continues comparing as long as `temp` is smaller than the current element.

# Thus, for `temp = 2`, it is compared with **every element in the sorted part `[8, 9, 87, 6543]`**, one by one, until it finds the correct position at the start of the list.