#calculate mean

# Replace ___ with your code
import numpy as np

# take user input
n = int(input())

# create a numpy array that contains only even numbers from 1 to n
array1 = np.arange(2, n + 1, 2)

# compute the mean of array1
result = np.mean(array1)

# display the resulting mean value
print(result)