#standard deviation calculate
import numpy as np

# Step 1: Create the NumPy array
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Step 2: Take 'n' as user input
n = int(input("Enter the value of n: "))

# Step 3: Get every nth element using slicing
nth_elements = array1[::n]

# Step 4: Calculate standard deviation
std_dev = np.std(nth_elements)

# Step 5: Display the results

print( std_dev)
