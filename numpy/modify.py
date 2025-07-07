#Modify Array Elements Using Slicing
import numpy as np

# Step 1: Take an integer n as input
n = int(input("Enter a number n: "))

# Step 2: Create an array from 0 to n (inclusive)
arr = np.arange(0, n )

# Step 3: Set every alternate number (starting from index 0) to 0
arr[::2] = 0

# Step 4: Display the resulting array
print( arr)
