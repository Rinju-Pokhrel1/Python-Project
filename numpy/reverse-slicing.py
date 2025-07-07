#slicing in reverse order
import numpy as np

# Step 1: Take input from the user and create a list
list1 = list(map(int, input("Enter numbers separated by space: ").split()))

# Step 2: Convert the list to a NumPy array
array1 = np.array(list1)

# Step 3: Slice to get elements at even indices (0, 2, 4, ...)
new_arr = array1[::2]

# Step 4: Reverse the new array
new_arr = new_arr[::-1]

# Step 5: Display the resulting array
print( new_arr)
