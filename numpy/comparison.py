#comparison 
import numpy as np

# take input for the elements of the first array
first = np.array(input().split(), dtype=int)
second = np.array(input().split(), dtype=int)

# use the less than or equal to operator
result = first<=second
print(result)

# use the greater than or equal to operator
result = first>=second
print(result)

# use the not equal to operator
result = first!=second
print(result)