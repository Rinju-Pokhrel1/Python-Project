#reshape 1D to 3D
import numpy as np

# create a 1D array
array1 = np.array([1, 2, 3, 4, 6, 7, 8, 9])

# reshape the 1D array to a 3D array
result = np.reshape(array1, (2, 2, 2))

# print the new array
print("1D to 3D Array: \n",result)