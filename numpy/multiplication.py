#element wise multiplication
import numpy as np

# Step 1: Take two lists as user input
list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

# Step 2: Convert the lists to NumPy arrays
arr1 = np.array(list1)
arr2 = np.array(list2)

# Step 3: Element-wise multiplication using * operator
result_operator = arr1 * arr2

# Step 4: Element-wise multiplication using multiply() function
result_function = np.multiply(arr1, arr2)

# Step 5: Print the results
print(result_operator)
print( result_function)
